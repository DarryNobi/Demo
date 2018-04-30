
var data=[];
for(var i in d_maps){

data.push(d_maps[i])

}

window.onload=function(){
    //默认获取当前日期
    var today = new Date();
    var nowdate = (today.getFullYear()) + "-" + (today.getMonth() + 1) + "-" + today.getDate();
    //对日期格式进行处理
    var date = new Date(nowdate);
    var mon = date.getMonth() + 1;
    var day = date.getDate();
    var mydate = date.getFullYear() + "-" + (mon < 10 ? "0" + mon : mon) + "-" + (day < 10 ? "0" + day : day);
    $(".nowdate").val(mydate);
    showList();
};
function showList(){

    var resultTab = $("#resultTab");
    var pubText="";
    data.forEach(function(item){
        if(item.isPublish)
          pubText="取消发布";
        else
          pubText="发布"
        $(
            '<tr/>', {
                'style' : 'font-size:18px'
            }).append($('<td/>', {
                text : item.id
            }))
            .append($('<td/>',{
                text : item.name
            }))
            .append($('<td/>',{
                text : item.gen_data
            }))
            .append($('<td/>',{
                text : item.SatelliteID
            }))
            .append($('<td/>',{
                text : item.type
            }))
            .append($('<td/>',{
                text : item.download
            }))
            .append($('<td/>')
            .append($('<p/>')
            .append($('<button/>',{
                'class' : 'operate',
                'id' : 'look' + item.id,
                text : '查看'
            }))
            .append($('<button/>',{
                'class' : 'operate',
                'id' : 'download' + item.id,
                text : '下载'
            }))
            .append($('<button/>',{
                'class' : 'operate',
                'id' : 'del' + item.id,
                text : '删除'
            }))
            .append($('<button/>',{
                'class' : 'publish',
                'id' : 'release' + item.id,
                'type':'submit',
                text: pubText
            }))
            ))
            .appendTo(resultTab);

    button=$("#release"+ item.id);
    button.on("click",{"num":item.id},changeStatus);
    });
};

function changeStatus(data){
    var id=data.data.num
    var button=$("#release"+id);
    var isPublish=button.text();
    if(isPublish=="发布"){
    button.text("发布中");
    button.attr("disabled",true);
    $.ajax({
          type: 'POST',
          url: '/uploadImage/',
          data: {ImageID:id},
          success:function(message){
          alert(message);
          button.removeAttr("disabled");
          if(message=="发布成功！")
               button.text("取消发布");
          else
               button.text("发布");
                                  },
          error:function(error){
          alert(error);
          }
    });}
    else if(isPublish=="取消发布"){
    button.text("正在取消");
    button.attr("disabled",true);
    $.ajax({
          type:'post',
          url: '/cancelPublish/',
          data: {ImageID:id},
          success:function(message){
          alert(message);
          button.removeAttr("disabled");
          if(message=="发布已取消！")
             button.text("发布");
          else
             button.text("取消发布");
                                  },
          error:function(error){
          alert(error);
          }
    });}
}
