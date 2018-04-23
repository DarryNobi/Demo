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
        var arr=e.target;//获取事件对象，即产生这个事件的元素-->ol.interaction.Select
        var collection = arr.getFeatures();//获取这个事件绑定的features-->返回值是一个ol.Collection对象
        var features = collection.getArray();//获取这个集合的第一个元素-->真正的feature
        if(features.length>0){
            var obj = features[0].getId();//获取之前绑定的ID,返回是一个json字符串
            var jsonobj=eval("("+obj+")");//转成json对象
            //alert(jsonobj.name);//获取ID
            //业务逻辑...
                 }
    }



    var doubleselectClick = new ol.interaction.Select({
        condition: ol.events.condition.doubleClick,
        style:changeStyle
    });
    map.addInteraction(doubleselectClick);
    selectClick.on("select",doubleClickEvent);
    function doubleClickEvent(e){
        var arr=e.target;//获取事件对象，即产生这个事件的元素-->ol.interaction.Select
        var collection = arr.getFeatures();//获取这个事件绑定的features-->返回值是一个ol.Collection对象
        var features = collection.getArray();//获取这个集合的第一个元素-->真正的feature
        if(features.length>0){
            var obj = features[0].getId();//获取之前绑定的ID,返回是一个json字符串
            var jsonobj=eval("("+obj+")");//转成json对象
            //alert(jsonobj.name);//获取ID
            //业务逻辑...
                 }
    }


});