$(function(){

                distance_btn_flag=true;
                var distance_source = new ol.source.Vector();
                var distance_vector;
                //定义一个交互式绘图对象
                var distance_draw;
                //创建一个交互式绘图对象
                distance_draw = new ol.interaction.Draw({
                    //绘制的数据源
                    source: distance_source,
                    //绘制类型
                    type: 'LineString',
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


                function distance_measure_init(){
                    //定义矢量图层
                    distance_vector = new ol.layer.Vector({
                        source: distance_source,
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
                    map_2.addLayer(distance_vector);


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
                    map_2.once('pointermove', pointerMoveHandler);



                    //创建测量提示框
                    createMeasureTooltip();

                    //定义一个事件监听
                    var listener;
                    //定义一个控制鼠标点击次数的变量
                    var count = 0;
                    //绘制开始事件

                    distance_draw.on('drawstart', function(evt){
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
                            if (geom instanceof ol.geom.LineString) {
                                //输出多线段的长度
                                output = formatLength(geom);
                                //Return the last coordinate of the geometry.
                                //获取多线段的最后一个点的坐标
                                tooltipCoord = geom.getLastCoordinate();
                            }

                            //设置测量提示框的内标签为最终输出结果
                            measureTooltipElement.innerHTML = output;
                            //设置测量提示信息的位置坐标
                            measureTooltip.setPosition(tooltipCoord);
                        });

                        //地图单击事件
                        map_2.on('singleclick', function (evt) {
                            //设置测量提示信息的位置坐标，用来确定鼠标点击后测量提示框的位置
                            measureTooltip.setPosition(evt.coordinate);
                            //如果是第一次点击，则设置测量提示框的文本内容为起点
                            if (count == 0) {
                                measureTooltipElement.innerHTML = "起点";
                            }
                           //根据鼠标点击位置生成一个点
                            var point = new ol.geom.Point(evt.coordinate);
                            //将该点要素添加到矢量数据源中
                            distance_source.addFeature(new ol.Feature(point));
                            //更改测量提示框的样式，使测量提示框可见
                            measureTooltipElement.className = 'tooltip tooltip-static';
                            //创建测量提示框
                            createMeasureTooltip();
                            //点击次数增加
                            count++;
                        });

                        //地图双击事件
                        map_2.on('dblclick', function (evt) {
                            //根据
                            var point = new ol.geom.Point(evt.coordinate);
                            distance_source.addFeature(new ol.Feature(point));
                        });
                    });


                    //绘制结束事件
                    distance_draw.on('drawend', function (evt) {
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
                        map_2.removeEventListener('singleclick');
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
                        map_2.addOverlay(measureTooltip);
                    }

                    //格式化测量长度
                    var formatLength = function (line) {
                        //定义长度变量
                        var length;

                            //Return the coordinates of the linestring.
                            //获取坐标串
                            var coordinates = line.getCoordinates();
                            //初始长度为0
                            length = 0;
                            //获取源数据的坐标系
                            var sourceProj = map_2.getView().getProjection();
                            //进行点的坐标转换
                            for (var i = 0; i < coordinates.length - 1; i++) {
                                //第一个点
                                var c1 = ol.proj.transform(coordinates[i], sourceProj, 'EPSG:4326');
                                //第二个点
                                var c2 = ol.proj.transform(coordinates[i + 1], sourceProj, 'EPSG:4326');
                                //获取转换后的球面距离
                                //Returns the distance from c1 to c2 using the haversine formula.
                                length += wgs84Sphere.haversineDistance(c1,c2);
                        }
                        //定义输出变量
                        var output;
                        //如果长度大于1000，则使用km单位，否则使用m单位
                        if (length > 1000) {
                            output = (Math.round(length / 1000 * 100) / 100) + ' ' + 'km'; //换算成KM单位
                        } else {
                            output = (Math.round(length * 100) / 100) + ' ' + 'm'; //m为单位
                        }
                        return output;
                        };
                 }

                distance_btn=document.getElementById("distance_button_div");
                distance_btn.onclick=function(){
                    distance_measure_init();
                    if(distance_btn_flag){
                        $("#draw_button_div").hide();
                        $("#area_button_div").hide();
                        map_2.addInteraction(distance_draw);
                        distance_btn_flag=false;
                        distance_btn.innerHTML="取消测距";
                    }
                    else{
                        $("#draw_button_div").show();
                        $("#area_button_div").show();
                        map_2.removeInteraction(distance_draw);
                        distance_vector.getSource().clear();
                        map_2.getOverlays().clear();
                        map_2.render();
                        distance_btn_flag=true
                        distance_btn.innerHTML="测距";
                    }
                }
});