
    var map = new ol.Map({
       target: 'map',
       view: new ol.View({
         center: ol.proj.fromLonLat([102.6, 20.2]),
         zoom: 13,
         maxZoom:17,
         minZoom:10
       }),
       controls: ol.control.defaults().extend([
            new ol.control.ScaleLine({  }),
            new ol.control.MousePosition({
                coordinateFormat: ol.coordinate.createStringXY(4),
                projection: 'EPSG:4326'
            }),
            new ol.control.ScaleLine({  }),
            new ol.control.ZoomSlider({
                maxResolution:1000,
                minResolution:1000
            })
      ]),
     });
    map.addLayer(default_geo_layer);
    map.addLayer(default_geo_layer2);
    //map.addLayer(geoserver_layer);
    //map.addLayer(geoserver_layer3);
    map.addLayer(geoserver_layer2);

    var map_2 =  map = new ol.Map({
        target:"map_2",
        view:map.getView(),
        layers:[
            new ol.layer.Tile({
                source: new ol.source.XYZ({
                    url:'http://t3.tianditu.cn/DataServer?T=img_w&X={x}&Y={y}&L={z}'
                }),
                projection: "EPSG:4326",
                id:"影像"
            })
        ]
    });

    var iscompare=false;
    var button_compare=$("#button_compare");
    var map1=$("#map");
    var map2=$("#map_2");

    button_compare.click(function(){
    if(iscompare){
        map1.off('mousemove');
        map2.off('mousemove');
        iscompare=false;
    }else{
        map1.on('mousemove',event_map1);
        map2.on('mousemove',event_map2);
        iscompare=true;
        }
    });



    function event_map1(e){
        //console.log(e);
        e.stopPropagation();
        var  offsetX=e.pageX,offsetY=e.y,width=document.body.clientWidth,height=document.body.clientHeight;
        console.log(offsetX);
        document.getElementById('map_2').style.clip='rect(0px,'+offsetX+'px,'+height+'px,0px)';
    }
    function event_map2(e){
        console.log(e);
        e.stopPropagation();
        var  offsetX=e.pageX,offsetY=e.y,width=document.body.clientWidth,height=document.body.clientHeight;
        document.getElementById('map_2').style.clip='rect(0px,'+offsetX+'px,'+height+'px,0px)';
    }
