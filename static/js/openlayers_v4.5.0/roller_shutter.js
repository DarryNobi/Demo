 var status1=true;
 var status2=true;
    var map_1 =  map = new ol.Map({
        target:"map_1",
        view:new ol.View({
            projection: "EPSG:4326",
            //center:[115.7555794477557, 22.6070466884657],
            center: [117.45, 39.25],
            zoom:15
        }),
        layers:[
            new ol.layer.Tile({source:new ol.source.OSM()})
        ]
    });
    var map_2 =  map = new ol.Map({
        target:"map_2",
        view:map_1.getView(),
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
   $("#map_1").on("mousemove",function(e){
        //console.log(e);
        e.stopPropagation();
        var  offsetX=e.x,offsetY=e.y,width=document.body.clientWidth,height=document.body.clientHeight;
        document.getElementById('map_2').style.clip='rect(0px,'+offsetX+'px,'+height+'px,0px)';
    });
     $("#map_2").on("mousemove",function(e){
        //console.log(e);
        e.stopPropagation();
        var  offsetX=e.x,offsetY=e.y,width=document.body.clientWidth,height=document.body.clientHeight;
        document.getElementById('map_2').style.clip='rect(0px,'+offsetX+'px,'+height+'px,0px)';
    });
    function roller(data){
    var id=data.data.id;
    var status=data.data.status;
    is(status){
    $("#id").on("mousemove",function(e){
        //console.log(e);
        e.stopPropagation();
        var  offsetX=e.x,offsetY=e.y,width=document.body.clientWidth,height=document.body.clientHeight;
        document.getElementById('map_2').style.clip='rect(0px,'+offsetX+'px,'+height+'px,0px)';
    });
    status
    }else


    }