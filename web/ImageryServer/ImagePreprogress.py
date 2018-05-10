import os
import numpy as np
import re
import gdal
from web.models import Map

def preprogress():
    imageList = Map.objects.filter(IsUnit8=0,Maptype='多光谱')
    gdal.AllRegister()
    driver = gdal.GetDriverByName("GTiff")
    count=0
    for image in imageList:
        if(count==1):
            break
        rpcFile=open(image.filepath.replace('.tiff','.rpb'),'r')
        text=rpcFile.readlines()
        for line in text:
            hoffLine=re.search(r'heightOffset = ([+|-|\d]\d+.?\d+)',line)
            if hoffLine:
                hoff=hoffLine.group(1)
                break
        rpcFile.close()
        RpcHeight="['RPC_HEIGHT="+str(hoff)+"]'"

        warpOP = gdal.WarpOptions(dstSRS='WGS84', rpc=True, multithread=True, errorThreshold=0.0,creationOptions=['Tiled=yes'],
                                  resampleAlg=gdal.gdalconst.GRIORA_Cubic,transformerOptions=RpcHeight,dstAlpha=True)
        imageDS = gdal.Open(image.filepath.encode('utf-8'),gdal.GA_ReadOnly)
        imageWithSRS = os.path.join(image.folder, image.name[:image.name.find('.tif')] + 'S.tif')

        srcDS = gdal.Warp(imageWithSRS.encode('utf-8').decode(), imageDS, options=warpOP)
        imageDS=None
        GeoTran = srcDS.GetGeoTransform()
        Project = srcDS.GetProjectionRef()

        bandcount = srcDS.RasterCount
        im_width = srcDS.RasterXSize
        im_height = srcDS.RasterYSize

        dstDS = driver.Create(imageWithSRS.replace('S.tif','R.tif'),
                              xsize=im_width, ysize=im_height, bands=bandcount-1, eType=gdal.GDT_Byte)

        dstDS.SetGeoTransform(GeoTran)
        dstDS.SetProjection(Project)


        for iband in range(1, 4):

             imgMatrix = srcDS.GetRasterBand(iband).ReadAsArray(0, 0, im_width, im_height)
             nodataMatrix=imgMatrix != 65535
             orginMatrix = imgMatrix[nodataMatrix]
             zeros = np.size(imgMatrix) - np.count_nonzero(imgMatrix)
             minVal = np.percentile(orginMatrix, float(zeros/nodataMatrix.sum()) * 100 + 0.15)
             maxVal = np.percentile(orginMatrix, 99.988)

             nodataMatrix = None
             orginMatrix = None

             idx1 = imgMatrix < minVal
             idx2 = imgMatrix > maxVal
             idx3 = ~idx1 & ~idx2
             imgMatrix[idx1] = imgMatrix[idx1] * 20 / minVal
             imgMatrix[idx3] = pow((imgMatrix[idx3] - minVal) / (maxVal - minVal), 0.7) * 255
             imgMatrix[idx2] = 255

             dstDS.GetRasterBand(iband).WriteArray(imgMatrix)
             dstDS.FlushCache()

             imgMatrix=None
        dstDS.GetRasterBand(4).WriteArray(srcDS.GetRasterBand(5).ReadAsArray(0, 0, im_width, im_height))
        dstDS.FlushCache()
        srcDS=None
        warpOP = gdal.WarpOptions(creationOptions=['Tiled=yes'])
        RTDS=gdal.Warp(imageWithSRS.replace('S.tif','RT2.tif').encode('utf-8').decode(), dstDS, options=warpOP)
        dstDS=None
        RTDS=None
        count+=1
        #Map.objects.filter(id=image.id).update(IsUnit8=1)
        #os.remove(imageWithSRS)
        #os.remove(imageWithSRS.replace('S.tif','R.tif'))

