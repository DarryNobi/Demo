
    var data = [];
    function query(){
    var query_name = $("#name").val()
    var query_type = $("#type").val()
    $.ajax({
            type:'get',
            url:'/_gs_show_list/',
            data: {
                'query_name':query_name,
                'query_type':query_type,
            },
            success:function(result){
                data=[];
                result_data=result['data'];
                for(var i in result_data)
                    data.push(result_data[i]);
                showList();
                },
            error:function(){
                alert('error')}
         });
    }

    function showList() {
        var graphicTab = $("#graphic_tab");
        data.forEach(function(item){
            $(
                '<tr/>', {
                    'class' : 'grap_tr'
                }).append($('<td/>', {
                    text : item.id
                }))
                .append($('<td/>',{
                    text : item.name
                }))
                .append($('<td/>',{
                    text : item.grahpictype
                }))
                .append($('<td/>',{
                    text : item.grahpiclabel
                }))
                .append($('<td/>',{
                    text : item.square
                }))
                .append($('<td/>',{
                    text : item.coordinate_x+item.coordinate_y
                }))
                .append($('<td/>',{
                    text : item.discrib
                }))
                .append($('<td/>')
                .append($('<p/>')
                .append($('<button/>',{
                    'class' : 'operate',
                    text : '修改'
                }))
                .append($('<button/>',{
                    'class' : 'operate',
                    text : '删除'
                }))))
                .appendTo(graphicTab);
        });
    }

    window.onload = function() {
        showList();
    }


    var query_btn = $("#query_btn")
    query_btn.click(function(){
        query();
    });