function showList(){

    var resultTab = $("#resultTab");
    var pubText="";
    data.forEach(function(item){
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