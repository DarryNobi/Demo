    var polygon = new ol.geom.Polygon([[[110, 39], [116, 39], [116, 33], [110, 33], [110, 39]]]);
    polygon.applyTransform(ol.proj.getTransform('EPSG:4326', 'EPSG:3857'));
    var feature = new ol.Feature(polygon);

    var vectorSource = new ol.source.Vector();
    vectorSource.addFeature(feature);

    var vectorLayer = new ol.layer.Vector({
        source: vectorSource
    });
    map.addLayer(vectorLayer);



var map = new ol.Map({
    target: 'map',
    layers: [
        vector
    ],
    view: new ol.View({
          center: ol.proj.transform([120,31], 'EPSG:4326', 'EPSG:3857'),
          zoom: 12
    })
});

var draw = new ol.interaction.Draw({
    source: source,
    type: 'Polygon',
    style: new ol.style.Style({
        fill: new ol.style.Fill({
            color: 'rgba(255, 255, 255, 0.2)'
        }),
        stroke: new ol.style.Stroke({
            color: '#ffcc33',
            width: 2
        }),
        image: new ol.style.Circle({
            radius: 7,
            fill: new ol.style.Fill({
                color: '#ffcc33'
            })
        })
    })
})
map.addInteraction(draw);