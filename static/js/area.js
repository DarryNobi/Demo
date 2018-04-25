$(function(){
                area_btn_flag=true;
                var area_source = new ol.source.Vector();
                var area_vector;
                //定义一个交互式绘图对象
                var area_draw;
                //创建一个交互式绘图对象
                area_draw = new ol.interaction.Draw({
                    //绘制的数据源
                    source: area_source,
                    //绘制类型
                    type: 'Polygon',
                    //样式
                    style: new ol.style.Style({
                        fill: new ol.style.Fill({
                            color:'rgba(255,255,255,0.2)'
                        }),
                        stroke: new ol.style.Stroke({
                            color: 'rgba(0,0,0,0.5)',
                            lineDash: [10, 10],
                            width:2
                        }),
                        image: new ol.style.Circle({
                            radius: 5,
                            stroke: new ol.style.Stroke({
                                color:'rgba(0,0,0,0.7)'
                            }),
                            fill: new ol.style.Fill({
                                color: 'rgba(255,255,255,0.2)'
                            })
                        })
                    })
                });


                function area_measure_init(){
                    //定义矢量图层
                    area_vector = new ol.layer.Vector({
                        source: area_source,
                        style: new ol.style.Style({
                            fill: new ol.style.Fill({
                                color:'rgba(255,255,255,0.2)'
                            }),
                            stroke: new ol.style.Stroke({
                                color: '#e21e0a',
                                width:2
                            }),
                            image: new ol.style.Circle({
                                radius: 5,
                                fill: new ol.style.Fill({
                                    color:'#ffcc33'
                                })
                            })
                        })
                    });
                    //将矢量图层添加到地图中
                    map.addLayer(area_vector);


                    //创建一个WGS84球体对象
                    var wgs84Sphere = new ol.Sphere(6378137);
                    //创建一个当前要绘制的对象
                    var sketch = new ol.Feature();
                    //创建一个帮助提示框对象
                    var helpTooltipElement;
                    //创建一个测量提示框对象
                    var measureTooltipElement;
                    //创建一个测量提示信息对象
                    var measureTooltip;
                    //继续绘制线段的提示信息
                    var continueLineMsg = '点击继续绘制线段';

                    //鼠标移动触发的函数
                    var pointerMoveHandler = function (evt) {
                        //Indicates if the map is currently being dragged.
                        //Only set for POINTERDRAG and POINTERMOVE events. Default is false.
                        //如果是平移地图则直接结束
                        if (evt.dragging) {
                            return;
                        }

                        if (sketch) {
                            //Get the feature's default geometry.
                            //A feature may have any number of named geometries.
                            //获取绘图对象的几何要素
                            var geom = sketch.getGeometry();
                        }
                    };

                    //触发pointermove事件
                    map.once('pointermove', pointerMoveHandler);



                    //创建测量提示框
                    createMeasureTooltip();

                    //定义一个事件监听
                    var listener;
                    //定义一个控制鼠标点击次数的变量
                    var count = 0;
                    //绘制开始事件

                    area_draw.on('drawstart', function(evt){
                        //The feature being drawn.
                        sketch = evt.feature;
                        //提示框的坐标
                        var tooltipCoord = evt.coordinate;
                        //监听几何要素的change事件
                        //Increases the revision counter and dispatches a 'change' event.

                        listener = sketch.getGeometry().on('change', function (evt) {
                            //The event target.
                            //获取绘制的几何对象
                            var geom = evt.target;
                            //定义一个输出对象，用于记录面积和长度

                             var output;
                            if (geom instanceof ol.geom.Polygon) {
                                map.removeEventListener('singleclick');
                                map.removeEventListener('dblclick');
                                //输出多边形的面积
                                output = formatArea(geom);
                                //Return an interior point of the polygon.
                                //获取多变形内部点的坐标
                                tooltipCoord = geom.getInteriorPoint().getCoordinates();
                            }

                            //设置测量提示框的内标签为最终输出结果
                            measureTooltipElement.innerHTML = output;
                            //设置测量提示信息的位置坐标
                            measureTooltip.setPosition(tooltipCoord);
                        });

                        //地图单击事件
                        map.on('singleclick', function (evt) {
                            //设置测量提示信息的位置坐标，用来确定鼠标点击后测量提示框的位置
                            measureTooltip.setPosition(evt.coordinate);
                            //如果是第一次点击，则设置测量提示框的文本内容为起点
                            if (count == 0) {
                                measureTooltipElement.innerHTML = "起点";
                            }
                           //根据鼠标点击位置生成一个点
                            var point = new ol.geom.Point(evt.coordinate);
                            //将该点要素添加到矢量数据源中
                            area_source.addFeature(new ol.Feature(point));
                            //更改测量提示框的样式，使测量提示框可见
                            measureTooltipElement.className = 'tooltip tooltip-static';
                            //创建测量提示框
                            createMeasureTooltip();
                            //点击次数增加
                            count++;
                        });

                        //地图双击事件
                        map.on('dblclick', function (evt) {
                            //根据
                            var point = new ol.geom.Point(evt.coordinate);
                            area_source.addFeature(new ol.Feature(point));
                        });
                    });


                    //绘制结束事件
                    area_draw.on('drawend', function (evt) {
                        count = 0;
                        //设置测量提示框的样式
                        measureTooltipElement.className = 'tooltip tooltip-static';
                        //Set the offset for this overlay.
                        //设置偏移量
                        measureTooltip.setOffset([0, -7]);
                        //清空绘制要素
                        sketch = null;
                        //清空测量提示要素
                        measureTooltipElement = null;
                        //创建测量提示框
                        createMeasureTooltip();
                        //Removes an event listener using the key returned by on() or once().
                        //移除事件监听
                        ol.Observable.unByKey(listener);
                        //移除地图单击事件
                        map.removeEventListener('singleclick');

                        var geojson_c = new ol.format.GeoJSON();
                        var current_feature=evt.feature;
                        var geo = current_feature.getGeometry();
                        var coordinates=geo.getCoordinates();
                        var geostr = coordinates[0].join(";");
                        var container = document.getElementById('popup');
                        container.style.display="block"
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
                         }, this);


                    //创建测量提示框
                    function createMeasureTooltip() {
                        //创建测量提示框的div
                        measureTooltipElement = document.createElement('div');
                        measureTooltipElement.setAttribute('id','lengthLabel');
                        //设置测量提示要素的样式
                        measureTooltipElement.className = 'tooltip tooltip-measure';
                        //创建一个测量提示的覆盖标注
                        measureTooltip = new ol.Overlay({
                            element: measureTooltipElement,
                            offset: [0, -15],
                            positioning:'bottom-center'
                        });
                        //将测量提示的覆盖标注添加到地图中
                        map.addOverlay(measureTooltip);
                    }

                //格式化测量面积
                var formatArea = function (polygon) {
                    //定义面积变量
                    var area;
                    //如果大地测量复选框被勾选，则计算球面面积

                        //获取初始坐标系
                        var sourceProj = map.getView().getProjection();
                        //Make a complete copy of the geometry.
                        //Transform each coordinate of the geometry from one coordinate reference system to another.
                        //The geometry is modified in place. For example, a line will be transformed to a line and a circle to a circle.
                        //If you do not want the geometry modified in place, first clone() it and then use this function on the clone.
                        //克隆该几何对象然后转换坐标系
                        var geom = polygon.clone().transform(sourceProj, 'EPSG:4326');
                        //Return the Nth linear ring of the polygon geometry.
                        //Return null if the given index is out of range.
                        //The exterior linear ring is available at index 0 and the interior rings at index 1 and beyond.
                        //获取多边形的坐标系
                        var coordinates = geom.getLinearRing(0).getCoordinates();
                        //Returns the geodesic area for a list of coordinates.
                        //获取球面面积
                        area = Math.abs(wgs84Sphere.geodesicArea(coordinates));


                    //定义输出变量
                    var output;
                    //当面积大于10000时，转换为平方千米，否则为平方米
                    if (area > 10000) {
                        output = (Math.round(area/1000000*100)/100) + ' ' + 'km<sup>2</sup>';
                    } else {
                        output = (Math.round(area*100)/100) + ' ' + 'm<sup>2</sup>';
                    }
                    return output;
                };
}

                area_btn=document.getElementById("area_button_div");
                area_btn.onclick=function(){
                area_measure_init();
                if(area_btn_flag){
                $("#draw_button_div").hide();
                $("#distance_button_div").hide();
                map.addInteraction(area_draw);
                area_btn_flag=false;
                area_btn.innerHTML="取消测面积";
                }
                else{
                $("#draw_button_div").show();
                $("#distance_button_div").show();
                map.removeInteraction(area_draw);
                area_vector.getSource().clear();
                map.getOverlays().clear();
                map.render();
                area_btn_flag=true
                area_btn.innerHTML="测面积";
                }
                }
});