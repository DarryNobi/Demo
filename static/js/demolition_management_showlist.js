


    window.onload = function() {
        data=[];
        showList();
        query();
        var query_btn = $("#query_btn");
        query_btn.click(function(){
            query();

        });
    }



function showList(){

    $("#demolition_tab").bootstrapTable({
              striped: true,//开启条纹
              locale:'zh-CN',//中文支持
              pagination: true,//是否开启分页（*）
              pageNumber:1,//初始化加载第一页，默认第一页
              pageSize: 10,//每页的记录行数（*）
              pageList: [10, 25, 50, 100],//可供选择的每页的行数（*）
              sidePagination: "client", //分页方式：client客户端分页，server服务端分页（*）
              showRefresh:true,//刷新按钮
              search: false,
              data:data,
              columns: [
                  {field: 'numm', title:'序号', width:'10%', align:'center',formatter: function (value, row, index) {return index+1;}},
                  {field: 'name', title:'名称', width:'10%', align:'center'},
                  {field: 'square', title:'面积', width:'10%', align:'center'},
                  {field: 'graphiclabel', title:'类型', width:'10%', align:'center'},
                  {field: 'address', title:'现场地址', width:'20%', align:'center'},
                  {field: 'discrib', title:'细节描述', width:'10%', align:'center'},
                  {field: 'foundtime', title:'录入时间', width:'10%', align:'center'},
                  {field: 'graphic_provide', title:'处理人', width:'10%', align:'center'},
                  {field: 'tool',title: '操作', align: 'center',
                          formatter: function (value,row,index){
                              var element = "<a href='#' class='operate check_href' id='check"+row.id +"' data-id='"+row.id +"' onclick='jump2draw(\" "+row.id+" \")' onmouseover='check_mouseOver(\" "+row.id+" \")' onmouseout='check_mouseOut(\" "+row.id+" \")'>"
                              + "<img id='check_img"+row.id+"' class='nav-img' src='../static/img/check.png'>"
                              + "</a>"
                              + "<a href='#' class='operate delete_href' id='delete"+row.id +"' data-id='"+row.id +"' onclick='changeStatus(\" "+row.id+" \")' onmouseover='del_mouseOver(\" "+row.id+" \")' onmouseout='del_mouseOut(\" "+row.id+" \")'>"
                              + "<img id='del_img"+row.id+"' class='nav-img' src='../static/img/delete.png'>"
                              + "</a>";
                              return element;
                          },
                  }
              ],

          })
};

function check_mouseOver(data) {
    var num = parseInt(data);
    $("#check_img"+num).attr("src","../static/img/check1.png");
}

function check_mouseOut(data) {
    var num = parseInt(data);
    $("#check_img"+num).attr("src","../static/img/check.png");
}

function del_mouseOver(data) {
    var num = parseInt(data);
    $("#del_img"+num).attr("src","../static/img/delete1.png");
}

function del_mouseOut(data) {
    var num = parseInt(data);
    $("#del_img"+num).attr("src","../static/img/delete.png");
}

function query(){
    var query_name = $("#query_name").val()
    var query_type = $("#query_type").val()
    var query_time = $("#query_time").val()
    var query_address = $("#query_address").val()

    if(parent.parent.window.unsearched){
    var query_name = parent.parent.window.event_search_name;
    var query_time = parent.parent.window.event_search_time;
    var query_address = parent.parent.window.event_search_address;
    parent.parent.window.unsearched=false;
    }

    $.ajax({
            type:'get',
            url:'/_de_event_search/',
            data: {
                'query_name':query_name,
                'query_type':query_type,
                'query_time':query_time,
                'query_address':query_address,
            },
            success:function(result){

               data1=[];
                result_data=result['d_ib_draws'];

                var count=1;
                for(var i in result_data){
                    result_data[i]['num']=count;
                    count=count+1;
                    data1.push(result_data[i]);

                    }

              $("#demolition_tab").bootstrapTable('load',data1);
                },
            error:function(){
                alert('查询失败')}
         });
    }

function changeStatus(data){
    var num=data;
    $.ajax({
        url:'/_delete_draw/',
        data: {'id':num},
        success: function(){
            alert('删除成功！');
            $("#demolition_tab").bootstrapTable('remove',{
                field: 'id',
                values: [parseInt(data)],
            })
        }
    });
}
function jump2draw(data){

    var num=data;
    window.location.href="/demolition_plotting/?id="+num;

}