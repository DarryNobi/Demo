        <script>
                            var map_selected = true;
                            var image_selected = true;
                            $("#ib_map_compare").click(function(){
                                if (map_selected) {
                                    $(".map_compare_span").css({"background":"#ffffff","color":"black","outline":"none","border-left":"1px solid #a7a9ad"});
                                    map_selected = false;
                                    status( map_selected,image_selected);

                                } else {
                                    $(".map_compare_span").css({"background":"#0a86e1","color":"white","outline":"none","border-left":"1px solid #a7a9ad"});
                                    map_selected = true;
                                    status( map_selected,image_selected);
                                }
                            })

                            $("#ib_image_compare").click(function(){
                                if (image_selected) {
                                    $(".image_compare_span").css({"background":"#ffffff","color":"black","outline":"none","border-left":"1px solid #a7a9ad"});
                                    image_selected = false;
                                    status( map_selected,image_selected);
                                } else {
                                    $(".image_compare_span").css({"background":"#0a86e1","color":"white","outline":"none","border-left":"1px solid #a7a9ad"});
                                    image_selected = true;
                                     status( map_selected,image_selected);

                                }
                            })
                            function status(status1,status2){
                                if (status1 && !status2){
                                    map.addLayer(default_geo_layer3);
                                    map.removeLayer(default_geo_layer);
                                    map.removeLayer(default_geo_layer2);
                                    }
                               if(status1 && status2){
                                    map.addLayer(default_geo_layer);
                                    map.addLayer(default_geo_layer2);
                                    map.removeLayer(default_geo_layer3);
                                    }
                               if(!status1 && !status2){
                                    map.removeLayer(default_geo_layer);
                                    map.removeLayer(default_geo_layer2);
                                    map.removeLayer(default_geo_layer3);
                               }
                               if(!status1 && status2){
                                    map.removeLayer(default_geo_layer);
                                    map.addLayer(default_geo_layer2);
                                    map.removeLayer(default_geo_layer3);


                               }
                            };
                        </script>