#
# from geoserver.catalog import Catalog
# import urllib.request
# import tarfile
# from web.models import Map
# import os
# import time
# import shutil
#
# baseURL='/home/zhou/PycharmProjects/Demo/Maps'
#
# def uploadImage(ImageID):
#     try:
#         image = Map.objects.filter(id=ImageID)
#         cat = Catalog("http://localhost:8080/geoserver/rest/", 'admin', 'geoserver')
#         wkspce = cat.get_workspace(image[0].SatelliteID)
#         #
#         # cat.create_coveragestore(name=image[0].name[:image[0].name.find('.tif')], workspace=wkspce,
#         #                          data=image[0].filepath.replace('.tif', 'RT.tif'))
#         store=cat.get_store('GF2',workspace=wkspce)
#         Map.objects.filter(id=image[0].id).update(isPublish=1)
#         return "发布成功！"
#     except Exception as err:
#         return str(err)
# def cancelPublish(ImageID):
#     try:
#         image = Map.objects.filter(id=ImageID)
#         cat = Catalog("http://172.20.53.158:8080/geoserver/rest/", 'admin', 'geoserver')
#         cat.delete(cat.get_layer(image[0].name[:image[0].name.find('.tif')]))
#         cat.reload()
#
#         cat.delete(cat.get_store(image[0].name[:image[0].name.find('.tif')]))
#         cat.reload()
#         Map.objects.filter(id=image[0].id).update(isPublish=0)
#         return "发布已取消！"
#     except Exception as err:
#         return str(err)
# def downloadImage(ImageID):
#     try:
#         if Map.objects.filter(GlobeID=ImageID):
#             return "图像已下载"
#         url='http://172.20.53.158:8089/_download_map/?id='+str(ImageID)
#         downloadPath=os.path.join(baseURL,str(ImageID))+'.tar.gz'
#
#         urllib.request.urlretrieve(url,os.path.join(baseURL,str(ImageID))+'.tar.gz')
#         downloadFile=tarfile.open(os.path.join(baseURL,str(ImageID)+'.tar.gz'),'r')
#         extractFile=os.path.join(baseURL,ImageID)
#         if not os.path.exists(extractFile):
#             os.mkdir(extractFile)
#         for file in downloadFile:
#             downloadFile.extract(file,extractFile)
#         downloadFile.close()
#
#         listProperty = ['SatelliteID', 'SensorID', 'ReceiveTime', 'name', 'EarthEllipsoid',
#                         'TopLeftLatitude','TopLeftLongitude', 'TopRightLatitude', 'TopRightLongitude', 'BottomRightLatitude',
#                         'BottomRightLongitude','BottomLeftLatitude', 'BottomLeftLongitude', 'filepath', 'gen_date',
#                         'folder', 'isPublish', 'ProductLevel', 'GlobeID', 'ImageDesc',
#                         'jpgPath']
#         dicProperty={}
#         for file in os.listdir(extractFile):
#             if('.tif' in file):
#                 imagePath=os.path.join(extractFile,file)
#             elif('.jpg' in file):
#                 jpg=os.path.join(extractFile,file)
#             else:
#                 xml=os.path.join(extractFile,file)
#         dicProperty['name'] =os.path.basename(imagePath)
#         dicProperty['filepath'] = imagePath
#         dicProperty['folder'] = extractFile
#         dicProperty['gen_date'] = time.strftime('%Y-%m-%d', time.localtime(time.time()))
#         dicProperty['isPublish'] = False
#         dicProperty['GlobeID'] = ImageID
#         dicProperty['ImageDesc'] = 'Describe this Image'
#         dicProperty['jpgPath']=jpg
#
#         info = open(xml, 'r')
#         infoLine = info.readline()
#         while (len(dicProperty) != len(listProperty)):
#             propertyKey = infoLine[infoLine.find('<') + 1:infoLine.find('>')]
#             propertyValue = infoLine[infoLine.find('>') + 1:infoLine.find('</')]
#             if (propertyKey in listProperty):
#                 if (propertyKey != 'ReceiveTime'):
#                     dicProperty[propertyKey] = propertyValue
#                 else:
#                     dicProperty[propertyKey] = propertyValue[:propertyValue.find(" ")]
#             infoLine = info.readline()
#         image = Map.objects.create(SatelliteID=dicProperty['SatelliteID'],SensorID=dicProperty['SensorID'],
#                                    ReceiveTime=dicProperty['ReceiveTime'], name=dicProperty['name'],
#                                    EarthEllipsoid=dicProperty['EarthEllipsoid'],TopLeftLatitude=dicProperty['TopLeftLatitude'],
#                                    TopLeftLongitude=dicProperty['TopLeftLongitude'],TopRightLatitude=dicProperty['TopRightLatitude'],
#                                    TopRightLongitude=dicProperty['TopRightLongitude'],BottomRightLatitude=dicProperty['BottomRightLatitude'],
#                                    BottomRightLongitude=dicProperty['BottomRightLongitude'],BottomLeftLatitude=dicProperty['BottomLeftLatitude'],
#                                    BottomLeftLongitude=dicProperty['BottomLeftLongitude'], filepath=dicProperty['filepath'],
#                                    gen_date=dicProperty['gen_date'],folder=dicProperty['folder'],
#                                    isPublish=dicProperty['isPublish'], ProductLevel=dicProperty['ProductLevel'],
#                                    GlobeID=dicProperty['GlobeID'],jpgPath=dicProperty['jpgPath'])
#         image.save()
#
#         info.close()
#
#         cat = Catalog("http://172.20.53.158:8080/geoserver/rest/", 'admin', 'geoserver')
#         wkspce = cat.get_workspace('GF2')
#         cat.create_coveragestore_external_geotiff(name=ImageID,data='file://'+imagePath.encode('utf-8').decode(),
#                                                   workspace=wkspce)
#         Map.objects.filter(GlobeID=ImageID).update(isPublish=1)
#
#         return ('下载成功！')
#
#     except Exception as err:
#         if Map.objects.filter(GlobeID=ImageID):
#             image = Map.objects.get(GlobeID=ImageID)
#             cat = Catalog("http://172.20.53.158:8080/geoserver/rest/", 'admin', 'geoserver')
#             if cat.get_layer(image.GlobeID):
#                 cat.delete(cat.get_layer(image.GlobeID))
#                 cat.reload()
#             if cat.get_store(name=str(image.GlobeID), workspace=image.SatelliteID):
#                 cat.delete(cat.get_store(name=str(image.GlobeID), workspace=image.SatelliteID))
#                 cat.reload()
#
#             Map.objects.get(GlobeID=ImageID).delete()
#             shutil.rmtree(os.path.join(baseURL, str(ImageID)))
#             os.remove(os.path.join(baseURL, str(ImageID) + '.tar.gz'))
#         return str(err)
#
#
# def deleteImage(ImageID):
#     try:
#         if not Map.objects.filter(GlobeID=ImageID):
#             return "请先下载图像"
#         image = Map.objects.get(GlobeID=ImageID)
#         cat = Catalog("http://172.20.53.158:8080/geoserver/rest/", 'admin', 'geoserver')
#         if cat.get_layer(image.GlobeID):
#             cat.delete(cat.get_layer(image.GlobeID))
#             cat.reload()
#         if cat.get_store(name=str(image.GlobeID),workspace=image.SatelliteID):
#             cat.delete(cat.get_store(name=str(image.GlobeID),workspace=image.SatelliteID))
#             cat.reload()
#
#         Map.objects.get(GlobeID=ImageID).delete()
#         shutil.rmtree(os.path.join(baseURL,str(ImageID)))
#         os.remove(os.path.join(baseURL,str(ImageID)+'.tar.gz'))
#
#         return "图片已删除！"
#     except Exception as err:
#         return str(err)
