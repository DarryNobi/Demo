$(function(){
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

    var map_2 = new ol.Map({
        target:"map_2",
        view:map.getView(),
        layers:[ new ol.layer.Tile({source:new ol.source.OSM()}) ]
    });

    function event_map1(e){
        //console.log(e);
        e.stopPropagation();
        var  offsetX=e.pageX,offsetY=e.y,width=document.body.clientWidth,height=document.body.clientHeight;
        console.log(offsetX);
        document.getElementById('map_2').style.clip='rect(0px,'+offsetX+'px,'+height+'px,0px)';
    }
    function event_map2(e){
        //console.log(e);
        e.stopPropagation();
        var  offsetX=e.pageX,offsetY=e.y,width=document.body.clientWidth,height=document.body.clientHeight;
        document.getElementById('map_2').style.clip='rect(0px,'+offsetX+'px,'+height+'px,0px)';
    }
});