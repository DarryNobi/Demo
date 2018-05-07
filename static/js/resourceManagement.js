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

var resource_tab = $("#resource_tab");

function showList(){
    resource_tab.bootstrapTable({
        locale:'zh-CN',//中文支持
        pagination: true,//是否开启分页（*）
        pageNumber:1,//初始化加载第一页，默认第一页
        pageSize: 3,//每页的记录行数（*）
        pageList: [10, 25, 50, 100],//可供选择的每页的行数（*）
        sidePagination: "client", //分页方式：client客户端分页，server服务端分页（*）
        showRefresh:false,//刷新按钮
        search: false,
        data:data,
        columns: [
            {field: 'id', title:'序号', width:'10%', align:'center'},
            {field: 'name', title:'影像资源', width:'10%', align:'center'},
            {field: 'gen_data', title:'入库时间', width:'10%', align:'center'},
            {field: 'SatelliteID', title:'卫星', width:'10%', align:'center'},
            {field: 'type', title:'影像类别', width:'20%', align:'center'},
            {field: 'download', title:'下载次数', width:'10%', align:'center'},
            {field: 'tool',title: '操作', align: 'center',
                formatter: function (value,row,index){
                    var element;
                    if (row.isPublish) {
                        element = "<button class='operate' id='change_resource"+row.id +"' data-id='"+row.id +"'>修改</button>"
                            + "<button class='operate' id='download_resource"+row.id +"' data-id='"+row.id +"' onclick=''>下载</button>"
                            + "<button class='operate' id='delete_resource"+row.id +"' data-id='"+row.id +"' onclick='delete(\" "+row.id+" \")'>删除</button>"
                            + "<button class='operate' id='release"+row.id +"' data-id='"+row.id +"' onclick='release(\" "+row.id+" \")'>发布</button>";
                    } else {
                        element = "<button class='operate' id='change_resource"+row.id +"' data-id='"+row.id +"'>修改</button>"
                            + "<button class='operate' id='download_resource"+row.id +"' data-id='"+row.id +"' onclick=''>下载</button>"
                            + "<button class='operate' id='delete_resource"+row.id +"' data-id='"+row.id +"' onclick='delete_res(\" "+row.id+" \")'>删除</button>"
                            + "<button class='operate' id='release"+row.id +"' data-id='"+row.id +"' onclick='release(\" "+row.id+" \")'>取消发布</button>";
                    }
                    return element;
                },
            }
        ],

    })
};

function release(data){
    var id=parseInt(data);
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
        });
    }
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
                if(message=="发布已取消！"){
                    button.text("发布");
                } else {
                    button.text("取消发布");
                }
            },
                error:function(error){
                    alert(error);
                }
            });
    }
}
function delete_res (data) {};