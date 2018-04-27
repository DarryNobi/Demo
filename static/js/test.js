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
                    text : item.resource
                }))
                .append($('<td/>',{
                    text : item.date
                }))
                .append($('<td/>',{
                    text : item.user
                }))
                .append($('<td/>',{
                    text : item.load
                }))
                .append($('<td/>',{
                    text : item.satellite
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
                    text : '发布'
                }))
                .append($('<button/>',{
                    'class' : 'operate',
                    'id' : 'cancel_release' + item.id,
                    text : '取消发布'
                }))))
                .appendTo(resultTab);
                $("#look"+item.id).on("click", look);
                $("#download"+item.id).on("click", download);
                $("#del"+item.id).on("click", del);
                $("#release"+item.id).on("click", release);
                $("#cancel_release"+item.id).on("click", cancel_release);
        });
    };