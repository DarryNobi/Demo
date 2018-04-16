 function showLocation(){
            if(navigator.geolocation) {
                var geolocation = new BMap.Geolocation();
                geolocation.getCurrentPosition(function(r){
                    if(this.getStatus() == BMAP_STATUS_SUCCESS){
                        console.log(r);
                        var locate = ol.proj.transform([r.point.lng, r.point.lat], 'EPSG:4326', 'EPSG:3857');
                        view.setCenter(locate);
                        view.setZoom(18);
                        var feature = new ol.Feature({
                            geometry: new ol.geom.Point(locate)
                        });
                        var source = new ol.source.Vector({
                            features:[feature]
                        });
                        vector.setSource(source);
                    }
                    else {
                        alert("定位失败，失败原因为："+this.getStatus());
                    }
                },{enableHighAccuracy: true});
            }
            else{
                alert("对不起，您的浏览器不支持定位！");
            }
        }