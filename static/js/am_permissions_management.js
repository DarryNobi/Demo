
    var data = [];

    for(var i in back_data){
        data.push(back_data[i])
    }

    var author_manage = $("#author_manage");

    /*判断是否有搜索条件，根据搜索条件去渲染表格*/
    window.onload=function(){
            author_manage.bootstrapTable({
				  locale:'zh-CN',//中文支持
				  pagination: true,//是否开启分页（*）
				  pageNumber:1,//初始化加载第一页，默认第一页
				  pageSize: 3,//每页的记录行数（*）
				  pageList: [10, 25, 50, 100],//可供选择的每页的行数（*）
				  sidePagination: "client", //分页方式：client客户端分页，server服务端分页（*）
				  showRefresh:true,//刷新按钮
				  search: true,
				  data:data,
				  columns: [
					  {field: 'id', title:'序号',width:'10%', align: 'center'},
					  {field: 'username', title:'帐号',width:'10%', align: 'center'},
					  {field: 'department_name', title:'单位名称',width:'10%', align: 'center'},
					  {field: 'user_permissions', title:'已有权限',width:'30%', align: 'center'},
					  {field: 'tool', title:'状态',width:'10%', align: 'center',
					  	  formatter:function(value,row,index){
					  	      var statusSel;
					  	  	      if (row.is_active) {
					  	  	          statusSel = "<select id='status" + row.id + "' class ='status' onchange='status_confirm(\" "+row.id+" \")'>"
                                      +"<option id='openSta" + row.id + "' value='启用' selected='selected'>启用</option>"
                                      +"<option id='closeSta" + row.id + "' value='禁用'>禁用</option>"
                                      +"</select>";
					  	  	      } else {
					  	  	      	  statusSel = "<select id='status" + row.id + "' class ='status' onchange='status_confirm(\" "+row.id+" \")'>"
                                      +"<option id='openSta" + row.id + "' value='启用'>启用</option>"
                                      +"<option id='closeSta" + row.id + "' value='禁用' selected='selected'>禁用</option>"
                                      +"</select>";
					  	  	      }
					  	  	      return statusSel;
							  }
					  },
					  {field: 'tool',title: '修改权限', align: 'center',width:'15%',
						  	  formatter: function (value,row,index){
						  	      var element;
						  	      if (row.is_active) {
						  	         element = "<p>"
                                      + "用户管理" + "<input class='authorityList" + row.id +"' type='checkbox' name='checkbox" + row.id + "' value='1' />"
                                      + "违建管理" + "<input class='authorityList" + row.id +"' type='checkbox' name='checkbox" + row.id + "' value='2' /></p><p>"
                                      + "拆迁管理" + "<input class='authorityList" + row.id +"' type='checkbox' name='checkbox" + row.id + "' value='3' />"
                                      + "资源管理" + "<input class='authorityList" + row.id +"' type='checkbox' name='checkbox" + row.id + "' value='4' /></p><p>"
                                      + "<button type='button' id='subBut" + row.id + "' class='btn btn-primary subBut' onclick='permission_confirm(\" "+row.id+" \",\" "+index+" \")'>确认</button>&nbsp&nbsp&nbsp&nbsp&nbsp"
                                      + "</p>";
						  	      } else {
						  	         element = "<p>"
                                      + "用户管理" + "<input class='authorityList" + row.id +"' type='checkbox' disabled='disabled' name='checkbox" + row.id + "' value='1' />"
                                      + "违建管理" + "<input class='authorityList" + row.id +"' type='checkbox' disabled='disabled' name='checkbox" + row.id + "' value='2' /></p><p>"
                                      + "拆迁管理" + "<input class='authorityList" + row.id +"' type='checkbox' disabled='disabled' name='checkbox" + row.id + "' value='3' />"
                                      + "资源管理" + "<input class='authorityList" + row.id +"' type='checkbox' disabled='disabled' name='checkbox" + row.id + "' value='4' /></p><p>"
                                      + "<button type='button' id='subBut" + row.id + "' disabled='disabled' class='btn btn-primary subBut' onclick='permission_confirm(\" "+row.id+" \",\" "+index+" \")'>确认</button>&nbsp&nbsp&nbsp&nbsp&nbsp"
                                      + "</p>";
						  	      }
								  return element;
						  	  },
					  }
				  ],

			  })

    }



function status_confirm(data){
    var mes="您确定修改吗？";
    if(confirm(mes)==true){
        var num = parseInt(data);
        var userid=data;
        var selectedVal1 = $("#status"+num).children('option:selected').val();
        var authList1 = $(".authorityList" + num);
        if (selectedVal1 === "禁用"){
            $("#subBut" + num).attr("disabled",true);
            authList1.each(function(index, val){
                $(val).attr("disabled",true);
            });
            $.ajax({
                type:'post',
                url:'/status_revise/',
                data: {
                    "is_active":"False",
                    "id":num
                },
                dataType:'json',
                success:function(){
                    alert('success')
                },
                error:function(){
                    alert('fail')
                },
            });
        } else {
            $("#subBut" + num).removeAttr("disabled");
            authList1.each(function(index, val){
                $(val).removeAttr("disabled");
            });
            $.ajax({
                   type:'post',
                   url:'/status_revise/',
                   data:{
                   "is_active":"True",
                   "id":userid
               },
                   dataType:'json',
               success:function(){
                   alert('success')
                   },
                error:function(){
                    alert('fail')
                },

            });
        }
    }
}

function permission_confirm(userId,index){
    var mes="您确定修改吗？";
    if(confirm(mes)==true){
        var num = parseInt(userId);
        var index = parseInt(index);
        var userid=data;
        //jquery获取复选框值
        var permission_value =[];//定义一个数组
        $('input[name="checkbox' + num + '"]:checked').each(function(){//遍历每一个名字为interest的复选框，其中选中的执行函数
        permission_value.push($(this).val());//将选中的值添加到数组chk_value中
        });

        $.ajax({
            type:'post',
            url:'/permission_revise/',
            data: {
                "permission_value":JSON.stringify(permission_value),
                "id":num
            },
            dataType:'json',
            success:function(data){
               author_manage.bootstrapTable("updateRow",{
                    index:index,
                    row:data['user'],
                })
            },
            error:function(){
                alert("fail")
            }
        });
    }
}