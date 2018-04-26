import gdal
from web.models import Map
import os
import numpy as np
from geoserver.catalog import Catalog

def uploadImage():

    count = 0

    imageList = Map.objects.filter(isPublish=0, Maptype='融合')
    gdal.AllRegister()
    driver = gdal.GetDriverByName("GTiff")

    for image in imageList:
        if (count > 3):
            break
        rpcFile=open(image.filepath.)
        warpOP = gdal.WarpOptions(dstSRS='WGS84', rpc=True, multithread=True, dstNodata=65535, errorThreshold=0.0,
                                  creationOptions=['Tiled=yes'], resampleAlg=1,
                                  transformerOptions=RPC_HEIGHT)
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


        for iband in range(1, bandcount):

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
        srcDS=None
        warpOP = gdal.WarpOptions(creationOptions=['Tiled=yes'])
        RTDS=gdal.Warp(imageWithSRS.replace('S.tif','RT.tif').encode('utf-8').decode(), dstDS, options=warpOP)
        dstDS=None
        RTDS=None
        os.remove(imageWithSRS)
        os.remove(imageWithSRS.replace('S.tif','R.tif'))




        cat=Catalog("http://localhost:8080/geoserver/rest/",'admin','geoserver')
        wkspce=cat.get_workspace(image.SatelliteID)

        cat.create_coveragestore(name=image.name[:image.name.find('.tif')],workspace=wkspce,data=imageWithSRS.replace('S.tif','RT.tif'))
        #layer=cat.create_coveragestore2(name=image.name[:image.name.find('.tif')],workspace=wkspce)
        #layer.url=imageWithSRS.replace('S.tif','R.tif')
        #cat.save(layer)
        #cat.reload()
        count += 1
        Map.objects.filter(id=image.id).update(isPublish=True)