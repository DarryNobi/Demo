window.onload=function(){
 var status={{message}};
 alert(message);

    var css_selected={
        color: "#3178f5",
        background:"#ffffff",
        "border-radius":"10px 10px 0 0",
        outline:"none",
        border:"none"
    };
    var css_unselected={
        color: "#8a8a8a",
        background:"#e6e7ea",
        "border-radius":"10px 10px 0 0",
        outline:"none",
        border:"none"
    };
if(message=="1"){
lis[1].css(css_unselected);
        lis[0].css(css_selected);
        //change1();
        //restore2();
}
if(message=="2"){
lis[0].css(css_unselected);
        lis[1].css(css_selected);
        //change2();
        //restore1();
}

}