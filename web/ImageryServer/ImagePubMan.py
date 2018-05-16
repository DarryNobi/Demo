
from geoserver.catalog import Catalog
from web.models import Map
import urllib
import os

baseURL='/home/zhou/PycharmProjects/Demo/Maps'

def uploadImage(ImageID):
    try:
        image = Map.objects.filter(id=ImageID)
        cat = Catalog("http://localhost:8080/geoserver/rest/", 'admin', 'geoserver')
        wkspce = cat.get_workspace(image[0].SatelliteID)
        #
        # cat.create_coveragestore(name=image[0].name[:image[0].name.find('.tif')], workspace=wkspce,
        #                          data=image[0].filepath.replace('.tif', 'RT.tif'))
        store=cat.get_store('GF2',workspace=wkspce)
        Map.objects.filter(id=image[0].id).update(isPublish=1)
        return "发布成功！"
    except Exception as err:
        return str(err)
def cancelPublish(ImageID):
    try:
        image = Map.objects.filter(id=ImageID)
        cat = Catalog("http://localhost:8080/geoserver/rest/", 'admin', 'geoserver')
        cat.delete(cat.get_layer(image[0].name[:image[0].name.find('.tif')]))
        cat.reload()

        cat.delete(cat.get_store(image[0].name[:image[0].name.find('.tif')]))
        cat.reload()
        Map.objects.filter(id=image[0].id).update(isPublish=0)
        return "发布已取消！"
    except Exception as err:
        return str(err)
def downloadImage(ImageID):
    try:
        url='http://172.20.53.158:8089/?id=1'
        name=ImageID
        urllib.urlretrive(url,os.path.join(baseURL,name))
        return ('下载成功！')
    except Exception as err:
        return str(err)


def deleteImage(ImageID):
    try:
        image = Map.objects.filter(id=ImageID)
        Map.objects.filter(id=image[0].id).delete()
        return "图片已删除！"
    except Exception as err:
        return str(err)
