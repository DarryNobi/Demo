$(function(){
    var changeStyle = function(feature){
        var ftype=feature.get("featuretype");
        return new ol.style.Style({
                stroke:new ol.style.Stroke({
                    color: '#319FD3',
                    width: 1,
                }),
                fill: new ol.style.Fill({ //矢量图层填充颜色，以及透明度
                    color: 'rgba(255, 0, 0, 0.2)'
                }),
        });
    };
//var close= document.getElementById("close_login").onclick;
    var selectClick = new ol.interaction.Select({
        condition: ol.events.condition.singleClick,
        style:changeStyle,
        //removeCondition: close
    });
    map.addInteraction(selectClick);
    selectClick.on("select",singleClickEvent);
    function singleClickEvent(e){
        var coords=e.selected[0].getGeometry().getCoordinates();
        var id=e.selected[0].getProperties().id;

        //alert(e.selected[0].getProperties().id)
        $.get("/query_draw/",{'id':id}, function(ret){
            drawinfo=ret['drawinfo'];
            //alert(drawinfo.name)

            var square = $("#popup_info_square");
            var type = $("#popup_info_type");
            var address = $("#popup_info_address");
            var time = $("#popup_info_time");
            square.text(drawinfo.square);
            type.text(drawinfo.graphiclabel);
            address.text(drawinfo.address);
            time.text(drawinfo.foundtime);

            var popup_info = document.getElementById("popup_info");
            popup_info.style.display="block";
            var popup = new ol.Overlay({
              element:popup_info,
              autoPan: true,
              autoPanAnimation: {
                duration: 250   //当Popup超出地图边界时，为了Popup全部可见，地图移动的速度.
              }
            });
            popup.setPosition(coords[0][0]);
            //popup_info.innerHTML=drawinfo.name

            map.addOverlay(popup);
        });
    }



    var doubleselectClick = new ol.interaction.Select({
        condition: ol.events.condition.doubleClick,
        style:changeStyle,
        removeCondition:ol.events.condition.singleClick

    });
    map.addInteraction(doubleselectClick);
    doubleselectClick.on("select",doubleClickEvent);
    function doubleClickEvent(e){
        var coords=e.selected[0].getGeometry().getCoordinates();
        var id=e.selected[0].getProperties().id;
//        var ishidden=true;
        var popup_button = document.getElementById("popup_button");
        var popup = new ol.Overlay({
          element:popup_button,
          autoPan: true,
          autoPanAnimation: {
            duration: 250   //当Popup超出地图边界时，为了Popup全部可见，地图移动的速度.
          }
        });
        popup.setPosition(coords[0][0]);

        popup_button.innerHTML="<p><button id='revise'>修改</button><button id='delete'>删除</button><button id='cancel'>取消</button></p>"

        map.addOverlay(popup);
//        if(ishidden){
//        map.addOverlay(popup);
//        ishidden=flase;
//        }else{
//        map.removeOverlay(popup);
//        ishidden=true;
//
//        }



        var revise = document.getElementById("revise");
        var remove = document.getElementById("delete");
        var cancel1 = document.getElementById("cancel");

        var container = document.getElementById('popup');
//        if(container.style.display="none"){
//           container.style.display="inline";
//        }
        var name = $("#name");
        var graphictype = $("#graphictype");
        var graphiclabel = $("#graphiclabel");
        var discrib =$("#discrib");
        var square = $("#square");
        var foundtime = $("#foundtime");
        var address = $("#graphicaddress");
        var save_button=$("#save_submit");
        var update_button=$("#save_update");
        var cancel = document.getElementById("save_cancel");
        cancel.onclick=function(){
        container.style.display="none";
        map.removeInteraction(doubleselectClick);
        map.addInteraction(doubleselectClick);
        }
         revise.onclick=function(){
//         container.style.display="none";
          popup_button.innerHTML='';

         $.get("/query_draw/",{'id':id}, function(ret){
            drawinfo=ret['drawinfo'];
             name.val(drawinfo.name);
         graphictype.val(drawinfo['graphictype']);
         graphiclabel.val(drawinfo['graphiclabel']);
         discrib.val(drawinfo.discrib);
         square.val(drawinfo.square);
         foundtime.val(drawinfo.foundtime);
         address.val(drawinfo.address);
         });

         container.style.display="block";

         save_button.hide();
         update_button.show();
         var overlay = new ol.Overlay(/** @type {olx.OverlayOptions} */ ({
            element: container,
            autoPan: true,
            autoPanAnimation: {
                duration: 250   //当Popup超出地图边界时，为了Popup全部可见，地图移动的速度.
            }
        }));
        overlay.setPosition(coords[0][0]);
        map.addOverlay(overlay);
          var update = document.getElementById("save_update");
        update.onclick=function(){
            var name = document.getElementById("name").value;
            var graphictype = document.getElementById("graphictype").value;
            var graphiclabel = document.getElementById("graphiclabel").value;
            var discrib = document.getElementById("discrib").value;
            var foundtime = document.getElementById("foundtime").value;
            var address = document.getElementById("graphicaddress").value;
            $.ajax({
                type:'post',
                url:'/update_draw/',
                data: {
                    'id':id,
                    'name':name,
                    'graphictype':graphictype,
                    'graphiclabel':graphiclabel,
                    'discrib':discrib,
                    'address':address
                },
                success:function(){
                    alert('修改成功');
                    //location.reload();
                    },
                error:function(){
                    alert('修改失败')}
             });
        }
        }
        remove.onclick=function(){
            $.get("/_delete_draw/",{'id':id}, function(ret){
                popup_button.innerHTML='';
            });
            location.reload();
        }
        cancel1.onclick=function(){
            popup_button.innerHTML='';
             map.removeInteraction(doubleselectClick);
             map.addInteraction(doubleselectClick);
        }
    }
      $("#close_login").click(function(){
            $("#popup_info").hide();
            map.removeInteraction(selectClick);
            map.addInteraction(selectClick);
        });

});
