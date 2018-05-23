
    var data = [];

    window.onload = function() {
        query();
        var query_btn = $("gra_btn")
        query_btn.click(function(){
            query();
        });
    }


    function query(){
    var query_name = $("#gra_name").val()
    var query_type = $("#gra_type").val()
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

    var graphicTab = $("#graphic_tab");

    function showList() {
        graphicTab.bootstrapTable({
              striped: true,//开启条纹
              locale:'zh-CN',//中文支持
              pagination: true,//是否开启分页（*）
              pageNumber:1,//初始化加载第一页，默认第一页
              pageSize: 10,//每页的记录行数（*）
              pageList: [10, 25, 50, 100],//可供选择的每页的行数（*）
              sidePagination: "client", //分页方式：client客户端分页，server服务端分页（*）
              showRefresh:false,//刷新按钮
              search: false,
              data:data,
              columns: [
                  {field: 'id', title:'序号', width:'10%', align:'center'},
                  {field: 'name', title:'名称', width:'10%', align:'center'},
                  {field: 'graphictype', title:'地物类别', width:'10%', align:'center'},
                  {field: 'graphiclabel', title:'标记类别', width:'10%', align:'center'},
                  {field: 'square', title:'面积', width:'20%', align:'center'},
                  {field: 'item.coordinate_x+item.coordinate_y', title:'经纬度', width:'10%', align:'center'},
                  {field: 'discrib', title:'描述', width:'10%', align:'center'},
                  {field: 'tool',title: '操作', align: 'center',
                          formatter: function (value,row,index){
                              var element = "<button class='operate' id='change_gs"+row.id +"' data-id='"+row.id +"'>修改</button>"
                              + "<button class='operate' id='delete_gs"+row.id +"' data-id='"+row.id +"' onclick='changeStatus(\" "+row.id+" \")'>删除</button>";
                              return element;
                          },
                  }
              ],

          })
    }

    function changeStatus(data){
        num=data;
        $.ajax({
            url:'/_delete_draw/',
            data: {'id':num},
            success: function(){
                alert('删除成功！');
                graphicTab.bootstrapTable('remove',{
                    field: 'id',
                    values: [parseInt(data)],
                })
            }
        });
    }