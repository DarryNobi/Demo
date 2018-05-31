$(function(){
    var btn=$("#btn");
    btn.click(function(){
     var name=$("#name").val();
      var type=$("#type").val();
       var nowdate=$("#nowdate").val();
        var address=$("#address").val();
        if(type=="1"){
        $.ajax({
        type:"post",
        url:'/_ib_event_search/',
        data:{
                'query_name':name,
                'query_type':type,
                'query_time':nowdate,
                'query_address':address,
                },
        success:function(result){
                data1=[];
                result_data=result['d_ib_draws'];
                ;
                var count=1;
                for(var i in result_data){
                    result_data[i]['num']=count;
                    count=count+1;
                    data1.push(result_data[i]);
                }
                },
        error:function(){
        alert("error");
        }





        });
    }else{


    }


    });
    });