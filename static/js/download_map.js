 function readBlobAsDataURL(blob, callback) {
            var a = new FileReader();
            a.onload = function (e) {
                callback(e.target.result);
            }
            a.readAsDataURL(blob);
        }




        $("#savemap").click(function () {
            map.once('postcompose', function (event) {
                var canvas = event.context.canvas;
                var SLT_pic = new ArrayBuffer();


                if (navigator.msSaveBlob) {
                    var ttt = canvas.msToBlob();//此处将图片转成二进制



                    readBlobAsDataURL(ttt, function (dataurl)
                    {
                        var name = "testpic.png";
                        post_webservice_async_json({ "oper": "SaveIMG","picname":name,"oge": dataurl });
                    })


                } else {
                    canvas.toBlob(function (blob) {
                        var mmm = blob;
                        alert("Binary pic",mmm);
                    });
                }
            });
            map.renderSync();
        });


        function post_webservice_async_json(paramObj) {
            var returnStr = "";
            var defer = $.Deferred();
            $.ajax({
                type: 'post',
                async: true,
                dataType: 'json',
                url: 'Test.ashx',
                traditional: true,
                data: { paramInfo: JSON.stringify(paramObj) },
                success: function (data) {
                    //alert("保存图层成功");
                    defer.resolve(data);
                }
            })
            return defer.promise();
        }
        string res;
        string paramInfo = null;
        paramInfo = context.Request.Form["paramInfo"];
        //图片读取
        if (paramInfo != null && paramInfo != "")
        {
            JavaScriptSerializer aa = new JavaScriptSerializer();


            Dictionary<string, string> dic = aa.Deserialize<Dictionary<string, string>>(paramInfo);


            string obj = dic["oge"].Replace(" ", "+").Split(',')[1];


            byte[] array = Convert.FromBase64String(obj);


            string oper = dic["oper"];
            string picname = dic["picname"];

          //图片保存到当前项目文件下
            MemoryStream ms = new MemoryStream(array);

            Image image = new Bitmap(ms);

            image.Save(context.Server.MapPath(@"~2.png"));
        }



