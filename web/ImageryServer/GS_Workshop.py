
'''from web.models import Map
from geoserver.catalog import Catalog
from web.models import Map

def uploadImage():

    count = 0

    imageList = Map.objects.filter(isPublish=0, Maptype='融合')
    cat=Catalog("http://localhost:8080/geoserver/rest/",'admin','geoserver')
    wkspce=cat.get_workspace(image.SatelliteID)

    cat.create_coveragestore(name=image.name[:image.name.find('.tif')],workspace=wkspce,data=imageWithSRS.replace('S.tif','RT.tif'))
        #layer=cat.create_coveragestore2(name=image.name[:image.name.find('.tif')],workspace=wkspce)
        #layer.url=imageWithSRS.replace('S.tif','R.tif')
        #cat.save(layer)
        #cat.reload()
        #Map.objects.filter(id=image.id).update(isPublish=True)'''