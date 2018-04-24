var map = new ol.Map({
       target: 'map',
       view: new ol.View({
         center: ol.proj.fromLonLat([102.56, 24.42]),
         zoom: 12,
         maxZoom:18,
         minZoom:5
       }),
       controls: ol.control.defaults().extend([
         new ol.control.ScaleLine({  }),
         new ol.control.MousePosition({
          coordinateFormat: ol.coordinate.createStringXY(4),
            projection: 'EPSG:4326'}),
        new ol.control.ScaleLine({  }),
        new ol.control.ZoomSlider({
        maxResolution:1000,
        minResolution:1000
          })
      ]),
     });
    //map.addLayer(baidu_layer);
    map.addLayer(default_geo_layer);
    map.addLayer(geoserver_layer);

location_btn=document.getElementById("location_btn");
location_btn.onclick=function location(){

    var lontitude=document.getElementById("lontitude").value;
    var lantitude=document.getElementById("lantitude").value;
    var newview=new ol.View({
         center: ol.proj.fromLonLat([lontitude, lantitude]),
         zoom: 12,
         maxZoom:18,
         minZoom:5
       });

    //view.setCenter([lontitude,lantitude]);
    alert(lontitude);


    //view.animate({zoom:view.getZoom()/4},{center:[lontitude,lantitude]},{zoom:view.getZoom()*4},{duration:2000} );
    map.setView(newview);
    map.render();
}