    var polygon = new ol.geom.Polygon([[[110, 39], [116, 39], [116, 33], [110, 33], [110, 39]]]);
    polygon.applyTransform(ol.proj.getTransform('EPSG:4326', 'EPSG:3857'));
    var feature = new ol.Feature(polygon);

    var vectorSource = new ol.source.Vector();
    vectorSource.addFeature(feature);

    var vectorLayer = new ol.layer.Vector({
        source: vectorSource
    });
    map.addLayer(vectorLayer);