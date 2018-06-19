var locate_btn=$("#locate");
locate_btn.click(function(){
var location=$("#location").val();
$.ajax({
type:"post",
url:"/locate/",
data:{
"location":location
},
success:function(location){
map.getView().animate({center:location});
},
error:function(){
alert("fail");
}


});










});