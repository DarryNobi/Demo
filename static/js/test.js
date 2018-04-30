 var d_maps={{ d_maps|safe }}
    var data=[]
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
                    'class' : 'operate',
                    'id' : 'release' + item.id,
                    'type':'submit',
                    'onClick':"$.ajax({"+
                            "type: 'POST',"+
                            "url: '/uploadImage/',"+
                            "data: {ImagePath:item.filepath},"+
                            "success: function(data){}"+
                            "});",
                    text: '发布'
                }))
                .append($('<button/>',{
                    'class' : 'operate',
                    'id' : 'cancel_release' + item.id,
                    text : '取消发布'
                }))))
                .appendTo(resultTab);
        });
    };