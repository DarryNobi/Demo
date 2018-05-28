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
        //alert(geostr);
 //默认获取当前日期
        var today = new Date();
        var nowdate = (today.getFullYear()) + "-" + (today.getMonth() + 1) + "-" + today.getDate();
        //对日期格式进行处理
        var date = new Date(nowdate);
        var mon = date.getMonth() + 1;
        var day = date.getDate();
        var mydate = date.getFullYear() + "-" + (mon < 10 ? "0" + mon : mon) + "-" + (day < 10 ? "0" + day : day);
        $("#foundtime").val(mydate);
        $("#foundtime").attr("diabled",true);
        var container = document.getElementById('popup');
        var save_button=$("#save_submit");
        var update_button=$("#save_update");
        container.style.display="block";
        update_button.hide();
        save_button.show();
        var overlay = new ol.Overlay(/** @type {olx.OverlayOptions} */ ({
            element: container,
            autoPan: true,
            autoPanAnimation: {
                duration: 250   //当Popup超出地图边界时，为了Popup全部可见，地图移动的速度.
            }
        }));
        var coordinate = coordinates[0][0];
        overlay.setPosition(coordinate);
        map.addOverlay(overlay);

        var submit = document.getElementById("save_submit");
        submit.onclick=function(){
            var name = document.getElementById("name").value;
            var graphictype = document.getElementById("graphictype").value;
            var graphiclabel = document.getElementById("graphiclabel").value;
            var discrib = document.getElementById("discrib").value;
            var square = document.getElementById("square").value;
            var address = document.getElementById("graphicaddress").value;
            $.ajax({
                type:'post',
                url:'/save_draw/',
                data: {
                    'coordi':geostr,
                    'name':name,
                    'graphictype':graphictype,
                    'graphiclabel':graphiclabel,
                    'discrib':discrib,
                    'square':square,
                    'address':address
                },
                success:function(){
                    alert('保存成功！');
                    location.reload();
                    },
                error:function(){
                    alert('保存失败');
                    }
              });
        }

        var cancel=document.getElementById("save_cancel");
        cancel.onclick=function(){
        container.style.display="none";
        }

    });




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