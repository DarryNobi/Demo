window.onload = function(){
    data=[];
    search();
    account_inquiry()

    $("#search_button").click(account_inquiry);
}

    function account_inquiry(){
		var message=$("#message").val();
		$.ajax({
            type:"post",
            url:"/_account_inquiry/",
            data:{"message":message},
            success:function(users){
                if(users["status"]){
                    data1=[];
                    users_temp=users["users"];
                    for(var i in users_temp){
                        data1.push(users_temp[i]);
                     }
                    $("#account_inquiry_tab").bootstrapTable('load',data1);
                }
            },
            error:function(){
                alert("error");
            }
		});
    }

	function search() {
		$("#account_inquiry_tab").bootstrapTable({
		      striped: true,//开启条纹
              locale:'zh-CN',//中文支持
              pagination: true,//是否开启分页（*）
              pageNumber:1,//初始化加载第一页，默认第一页
              pageSize: 10,//每页的记录行数（*）
              pageList: [10, 25, 50, 100],//可供选择的每页的行数（*）
              sidePagination: "client", //分页方式：client客户端分页，server服务端分页（*）
              showRefresh:false,//刷新按钮
              search: true,
              data:data,
              columns: [
                  {field: 'num', title:'帐号', width:'10%', align:'center'},
                  {field: 'username', title:'帐号', width:'10%', align:'center'},
                  {field: 'department_name', title:'部门', width:'10%', align:'center'},
                  {field: 'contact_usr', title:'联系人', width:'10%', align:'center'},
                  {field: 'phone', title:'联系电话', width:'10%', align:'center'},
                  {field: 'is_active', title:'状态', width:'10%', align:'center'},
                   {field: 'user_permissions', title:'权限', width:'10%', align:'center'},
              ],

          })
	}
