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

    var selectClick = new ol.interaction.Select({
        condition: ol.events.condition.singleClick,
        style:changeStyle
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

            var popup_info = document.getElementById("popup_info");
            var popup = new ol.Overlay({
              element:popup_info,
              autoPan: true,
              autoPanAnimation: {
                duration: 250   //当Popup超出地图边界时，为了Popup全部可见，地图移动的速度.
              }
            });
            popup.setPosition(coords[0][0]);
            popup_info.innerHTML=drawinfo.name
            map.addOverlay(popup);
        });
    }



    var doubleselectClick = new ol.interaction.Select({
        condition: ol.events.condition.doubleClick,
        style:changeStyle
    });
    map.addInteraction(doubleselectClick);
    doubleselectClick.on("select",doubleClickEvent);
    function doubleClickEvent(e){
        var coords=e.selected[0].getGeometry().getCoordinates();
        var id=e.selected[0].getProperties().id;

        var popup_info = document.getElementById("popup_button");
        var popup = new ol.Overlay({
          element:popup_button,
          autoPan: true,
          autoPanAnimation: {
            duration: 250   //当Popup超出地图边界时，为了Popup全部可见，地图移动的速度.
          }
        });
        popup.setPosition(coords[0][0]);

        popup_info.innerHTML="<p><button id='revise'>修改</button><button id='delete'>删除</button><button id='cancel'>取消</button></p>"
        map.addOverlay(popup);

        var revise = document.getElementById("popup_button");
        var remove = document.getElementById("popup_button");
        var cancel = document.getElementById("popup_button");
        revise.onclick=function(){
            ;
        }
        remove.onclick=function(){
            $.get("/delete_draw/",{'id':id}, function(ret){
                popup_info.innerHTML='';
            });
        }
        remove.onclick=function(){
            popup_info.innerHTML='';
        }
    }
});