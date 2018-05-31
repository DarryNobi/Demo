
$(function(){
var loc_button=$("#location_btn1");
loc_button.click(function(){
 var location=$("#location").val();
$.ajax({
type:"get",
url:"/locate/",
data:{
"location":location
},
success:function(data){
var lon=data["lon"];
var lat=data["lat"];
alert(lon);
alert(lat);
var location=ol.proj.fromLonLat([lon,lat]);
map.getView().animate({center:location});
},
error:function(){
alert("error");
}
});
});
});
