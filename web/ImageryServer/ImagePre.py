# import os,shutil
# import numpy as np
# import re
# import gdal
# from web.models import Map
#
# def preprogress():
#     imageList = Map.objects.filter(IsUnit8=0,Maptype='融合')
#     gdal.AllRegister()
#     driver = gdal.GetDriverByName("GTiff")
#     for image in imageList:
#         imageDS = gdal.Open(image.filepath.encode('utf-8'), gdal.GA_ReadOnly)
#         im_width = imageDS.RasterXSize
#         im_height = imageDS.RasterYSize
#         imageUnit8 = image.filepath.replace('.tif','U.tif')
#         dstDS = driver.Create(imageUnit8,
#                               xsize=im_width, ysize=im_height, bands=3, eType=gdal.GDT_Byte)
#
#         for iband in range(1, 4):
#             imgMatrix = imageDS.GetRasterBand(iband).ReadAsArray(0, 0, im_width, im_height)
#             zeros = np.size(imgMatrix) - np.count_nonzero(imgMatrix)
#             minVal = np.percentile(imgMatrix, float(zeros / np.size(imgMatrix) * 100 + 0.15))
#             maxVal = np.percentile(imgMatrix, 99.988)
#
#             idx1 = imgMatrix < minVal
#             idx2 = imgMatrix > maxVal
#             idx3 = ~idx1 & ~idx2
#             imgMatrix[idx1] = imgMatrix[idx1] * 20 / minVal
#             imgMatrix[idx3] = pow((imgMatrix[idx3] - minVal) / (maxVal - minVal), 0.7) * 255
#             imgMatrix[idx2] = 255
#
#             dstDS.GetRasterBand(iband).WriteArray(imgMatrix)
#             dstDS.FlushCache()
#             imgMatrix = None
#         imageDS = None
#         dstDS = None
#
#         shutil.copyfile(image.filepath.replace('.tif','_rpc.txt'),
#                         imageUnit8.replace('.tif', '_rpc.txt'))
#
#         rpcFile=open(image.filepath.replace('_fusion.tif','.rpb'),'r')
#         text=rpcFile.readlines()
#         for line in text:
#             hoffLine=re.search(r'heightOffset = ([+|-|\d]\d+.?\d+)',line)
#             if hoffLine:
#                 hoff=hoffLine.group(1)
#                 break
#         rpcFile.close()
#         RpcHeight="['RPC_HEIGHT="+str(hoff)+"]'"
#
#         warpOP = gdal.WarpOptions(dstSRS='WGS84', rpc=True, multithread=True, errorThreshold=0.0,creationOptions=['Tiled=yes'],
#                                   resampleAlg=gdal.gdalconst.GRIORA_Cubic,transformerOptions=RpcHeight,dstAlpha=True)
#         imageDS = gdal.Open(imageUnit8.encode('utf-8'),gdal.GA_ReadOnly)
#         imageRPC = os.path.join(image.folder, image.name[:image.name.find('.tif')] + 'R.tif')
#
#         srcDS = gdal.Warp(imageRPC.encode('utf-8').decode(), imageDS, options=warpOP)
#         imageDS=None
#         srcDS=None
#
#         os.remove(imageUnit8)
#         os.remove(imageUnit8.replace('.tif', '_rpc.txt'))
#
#         DS = gdal.Open(imageRPC.encode('utf-8').decode(), gdal.GA_Update)
#         iWidth = DS.RasterXSize
#         iHeigh = DS.RasterYSize
#         iPixelNum = iWidth * iHeigh
#         iTopNum = 4096
#         iCurNum = iPixelNum / 4
#         anLevels = []
#         nLevelCount = 0
#         while (iCurNum > iTopNum):
#             anLevels.append(pow(2, nLevelCount + 2))
#             nLevelCount += 1
#             iCurNum /= 4
#         DS.BuildOverviews(overviewlist=anLevels)
#         DS = None
#         Map.objects.filter(id=image.id).update(IsUnit8=1)
