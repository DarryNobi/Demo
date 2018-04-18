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
  $(function(){
    draw_btn_flag=true;
    draw_vector_layer=new ol.source.Vector();

    var draw = new ol.interaction.Draw({
        source: draw_vector_layer,
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
        }),
    });
    draw.on('drawend', function(e) {
        var geojson_c = new ol.format.GeoJSON();
        var current_feature=e.feature;
        var geo = current_feature.getGeometry();
        var coordinates=geo.getCoordinates();
        var geostr = coordinates[0].join(";");
        alert(geostr);
        $.ajax({
            type:'post',
            url:'/save_draw/',
            data: {
            'coordi':geostr},
            success:function(){
                alert('success')},
            error:function(){
                alert('error')}
        });
    });


   // document.getElementById("map").innerHTML = "<button id='draw_button_div'>标绘</button>"
    draw_btn=document.getElementById("draw_button_div");
    draw_btn.onclick=function(){
        if(draw_btn_flag){
        $("#distance_button_div").hide();
        $("#area_button_div").hide();
        map.addInteraction(draw);
        draw_btn_flag=false;
        draw_btn.innerHTML="取消标绘";
        }
        else{
        $("#distance_button_div").show();
        $("#area_button_div").show();
        map.removeInteraction(draw);
        draw_btn_flag=true
        draw_btn.innerHTML="标绘";
        }
    }
});

function save_data(geotype,geodata,name,type,time){

}