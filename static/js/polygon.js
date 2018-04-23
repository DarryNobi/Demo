 /*   var polygon = new ol.geom.Polygon([[[110, 39], [116, 39], [116, 33], [110, 33], [110, 39]]]);
    polygon.applyTransform(ol.proj.getTransform('EPSG:4326', 'EPSG:3857'));
    var feature = new ol.Feature(polygon);

    var vectorSource = new ol.source.Vector();
    vectorSource.addFeature(feature);

    var vectorLayer = new ol.layer.Vector({
        source: vectorSource
    });
    map.addLayer(vectorLayer);
*/
    draw_btn_flag=true;

    var draw = new ol.interaction.Draw({
        source: new ol.source.Vector(),
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
    });

    document.getElementById("map").innerHTML = "<button id='draw_button_div'>标绘</button>"
    draw_btn=document.getElementById("draw_button_div");
    draw_btn.onclick=function(){
        if(draw_btn_flag){
        map.addInteraction(draw);
        draw_btn_flag=false;
        draw_btn.innerHTML="取消标绘";
        }
        else{
        map.removeInteraction(draw);
        draw_btn_flag=true
        draw_btn.innerHTML="标绘";
        }
    }