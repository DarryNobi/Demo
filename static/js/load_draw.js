$(function(){
$.post("/load_all_draw/");

var all_draws={{ all_draws|safe }};
alert(all_draws);
});