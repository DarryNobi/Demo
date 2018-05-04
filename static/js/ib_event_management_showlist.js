
    var data = [];

    window.onload = function() {
        query();
        var query_btn = $("#query_btn")
        query_btn.click(function(){
            query();
        });
    }

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
                text : item.square
            }))
            .append($('<td/>',{
                text : item.graphictype
            }))
            .append($('<td/>',{
                text : item.coordinate_x+item.coordinate_y
            }))
            .append($('<td/>',{
                text : item.discrib
            }))
            .append($('<td/>',{
                text : item.graphic_provide_id
            }))
            .append($('<td/>',{
                text : '录入时间'
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
                'id' : 'delete' + item.id,
                text : '删除'
            }))
            ))
            .appendTo(resultTab);

    button=$("#delete"+ item.id);
    button.on("click",{"num":item.id},changeStatus);
    });
};

function query(){
    var query_name = $("#name").val()
    var query_type = $("#type").val()
    var query_time = $("#time").val()
    var query_address = $("#query_address").val()
    $.ajax({
            type:'get',
            url:'/_ib_event_search/',
            data: {
                'query_name':query_name,
                'query_type':query_type,
                'query_time':query_time,
                'query_address':query_address,
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

function changeStatus(data){
        num=data.data.num
        $.ajax({
          url:'/_delete_draw/',
          data: {'id':num},
          success: function(){
            alert('删除成功！');
            location.reload()
          }
        });
    }