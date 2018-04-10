
        var geoserver_layer = new ol.layer.Image({
              source: new ol.source.ImageWMS({
              url:'http://172.20.53.157:8080/geoserver/wms',
              projection:'EPSG:4326',
              params:{
                LAYERS: 'test:tran'}
              })
            });
        //172.20.53.157:8080/geoserver/wms