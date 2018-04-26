
        var geoserver_layer = new ol.layer.Image({
            source: new ol.source.ImageWMS({
                url:'http://172.20.53.157:8080/geoserver/wms',
                projection:'EPSG:4326',
                params:{
                LAYERS: 'test:resample'}
            }),
            projection: "EPSG:4326",
            opacity:0.5,
        });

        //172.20.53.157:8080/geoserver/wms

        var default_geo_layer2=new ol.layer.Tile({
            source: new ol.source.XYZ({
                url:'http://t3.tianditu.cn/DataServer?T=img_w&X={x}&Y={y}&L={z}'
            }),
            projection: "EPSG:4326",
            id:"影像",
            opacity:1,
        });

        var default_geo_layer = new ol.layer.Tile({
            source: new ol.source.OSM(),
            projection: "EPSG:4326",
            opacity:0.2,
        });