$(function(){

    selection1=document.getElementById("compare1");
    selection2=document.getElementById("compare2");
    $.ajax({
            type:'get',
            url:'/_map_inquiry/',
            data: {
            },
            success:function(d_maps){
                maps=JSON.parse(d_maps);
                for(m in maps){
                    name=maps[m].name;
                    id=maps[m].GlobeID;
                    selection1.add(new Option(name,id))
                    selection2.add(new Option(name,id))
                }
            }
         });



    var iscompare=false;
    var button_compare=$("#button_compare");
    var map1=$("#map");
    var map2=$("#map_2");
    button_compare.click(function(){
    if(iscompare){
        document.getElementById("map_2").style.display="none";//隐藏
        //map2.hide();
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
//        alert(value1);
//         alert(value2);

        var temp_layer1 = new ol.layer.Image({
            source: new ol.source.ImageWMS({
//              crossOrigin: 'anonymous',
                url:'http://172.20.53.157:8080/geoserver/wms',
                projection:'EPSG:4326',
                params:{
                LAYERS: value1.toString()}
            }),
            projection: "EPSG:4326",
           // opacity:0.5,
        });
        var temp_layer2 = new ol.layer.Image({
            source: new ol.source.ImageWMS({
//              crossOrigin: 'anonymous',
                url:'http://172.20.53.157:8080/geoserver/wms',
                projection:'EPSG:4326',
                params:{
                LAYERS: value2.toString()}
            }),
            projection: "EPSG:4326",
            //opacity:0.5,
        });

        map.addLayer(temp_layer1);
        map_2.addLayer(temp_layer2);
        map.render();
        map_2.render();

        document.getElementById("map_2").style.display="block";//显示
        //map2.show();
        map1.on('mousemove',event_map1);
        map2.on('mousemove',event_map2);
        iscompare=true;
        $("#compare_span").text('取消对比');
        }
    });
//    var map_1 = new ol.Map({
//        target:"map",
//        view:new ol.View({
//            projection: "EPSG:4326",
//            center:[115.7555794477557, 22.6070466884657],
//            //center: [117.45, 39.25],
//            zoom:15
//        }),
//        layers:[
//            new ol.layer.Tile({source:new ol.source.OSM()})
//        ]
//    });
//    map_2 = new ol.Map({
//        target:"map_2",
//        view:map.getView(),
//        layers:[ new ol.layer.Tile({source:new ol.source.OSM()}) ]
//    });

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