function open_link(frame_name,url){
    document.getElementById(frame_name).src = url;
}

function open_link(url){
    document.getElementById("context_container").src = url;
}

 //   var al_add_user = document.getElementById("adduser");
 //   al_add_user.onclick = function (e) {
 //   open_link('172.20.53.157:8088/add_usr');
 //   }

  //  var al_home = document.getElementById("home");
   // al_home.onclick = function (e) {
   // open_link('172.20.53.157:8088/map');
   // }