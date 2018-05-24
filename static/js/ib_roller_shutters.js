$(function(){

    $.ajax({
            type:'get',
            url:'/_map_inquiry/',
            data: {
            },
            success:function(d_maps){
            alert(d_maps);

            }
         });



    var iscompare=false;
    var button_compare=$("#button_compare");
    var map1=$("#map");
    var map2=$("#map_2");
    map1.on('mousemove',event_map1);
    map2.on('mousemove',event_map2);
    button_compare.click(function(){
    if(iscompare){
        document.getElementById("map_2").style.display="none";//隐藏
        //map2.hide();

        iscompare=false;
        $("#compare_span").text('开始对比');
    }else{
        document.getElementById("map_2").style.display="block";//显示
        //map2.show();

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
    map_2 = new ol.Map({
        target:"map_2",
        view:map.getView(),
        layers:[ new ol.layer.Tile({source:new ol.source.OSM()}) ]
    });
    function event_map2(e){
        console.log(e);
        e.stopPropagation();
        var  offsetX=e.pageX,offsetY=e.y,width=document.body.clientWidth,height=document.body.clientHeight;
        document.getElementById('map_2').style.clip='rect(0px,'+offsetX+'px,'+height+'px,0px)';
    }

    function event_map1(e){
        //console.log(e);
        e.stopPropagation();
        var  offsetX=e.pageX,offsetY=e.y,width=document.body.clientWidth,height=document.body.clientHeight;
        console.log(offsetX);
        document.getElementById('map_2').style.clip='rect(0px,'+offsetX+'px,'+height+'px,0px)';
    }

});