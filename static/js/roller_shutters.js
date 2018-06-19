$(function(){

    selection1=document.getElementById("compare1");
    selection2=document.getElementById("compare2");
    var maps_list;
    $.ajax({
            type:'get',
            url:'/_map_inquiry/',
            data: {
            },
            success:function(d_maps){
                maps_list=JSON.parse(d_maps);
                for(m in maps_list){
                    area=maps_list[m].Area;
                    time=maps_list[m].ReceiveTime;
                    id=maps_list[m].GlobeID;
                    selection1.add(new Option(area+time,id))

                    ////////////////////////////////////////////add all layers by default
                    temp_layer = new ol.layer.Image({
                        source: new ol.source.ImageWMS({
                          crossOrigin: 'anonymous',
                            url:'http://172.20.53.158:8080/geoserver/wms',
                            projection:'EPSG:4326',
                            params:{
                            LAYERS: id.toString()}
                        }),
                        projection: "EPSG:4326",
                       // opacity:0.5,
                    });
                    //map.addLayer(temp_layer);
                }
            }
         });
    selection1.onchange=function(){
        var index1 = selection1.selectedIndex;
        $("#compare2").empty();
        for(m in maps_list){
            area1=selection1.options[index1].text.replace(/[0-9]/g, '').replace(/[-]/g, '');
            if(maps_list[m].Area==area1){
                var area=maps_list[m].Area;
                var time=maps_list[m].ReceiveTime;
                    id=maps_list[m].GlobeID;
                selection2.add(new Option(area+time,id));
            }
        }
    };

    var iscompare=false;
    var button_compare=$("#button_compare");
    var map1=$("#map");
    var map2=$("#map_2");
    var temp_layer1;
    var temp_layer2;
    button_compare.click(function(){
    if(iscompare){
        map.removeLayer(temp_layer1);
        map_2.removeLayer(temp_layer2);

        map2.hide();
        map1.off('mousemove');
        map2.off('mousemove');
        iscompare=false;
        $("#compare_span").text('开始对比');
    }else{

        var index1 = selection1.selectedIndex;
        var text1 = selection1.options[index1].text;
        var value1 = selection1.options[index1].value;
        var index2 = selection2.selectedIndex;
        var text2 = selection2.options[index2].text;
        var value2 = selection2.options[index2].value;
        //alert(value1);
        //alert(value2);
        for(m in maps_list){
                    id=maps_list[m].GlobeID;
                    if(id==value2){
                        cord_x=(maps_list[m].TopLeftLongitude+maps_list[m].TopRightLongitude)/2.0;
                        cord_y=(maps_list[m].TopLeftLatitude+maps_list[m].BottomLeftLatitude)/2.0;
                        var location=ol.proj.fromLonLat([cord_x,cord_y]);
                        map.getView().animate({center:location,zoom:18});
                    }
                }

        temp_layer1 = new ol.layer.Image({
            source: new ol.source.ImageWMS({
              crossOrigin: 'anonymous',
                url:'http://172.20.53.158:8080/geoserver/wms',
                projection:'EPSG:4326',
                params:{
                LAYERS: value1.toString()}
            }),
            projection: "EPSG:4326",
           // opacity:0.5,
        });
        temp_layer2 = new ol.layer.Image({
            source: new ol.source.ImageWMS({
              crossOrigin: 'anonymous',
                url:'http://172.20.53.158:8080/geoserver/wms',
                projection:'EPSG:4326',
                params:{
                LAYERS: value2.toString()}
            }),
            projection: "EPSG:4326",
            //opacity:0.5,
        });

        map.addLayer(temp_layer2);
        map_2.addLayer(temp_layer1);

        map2.show();
        map2.css("visibility","visible");

        map1.on('mousemove',event_map1);
        map2.on('mousemove',event_map2);
        iscompare=true;
        $("#compare_span").text('取消对比');
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
});