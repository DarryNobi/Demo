function showList(){
    var graphicTab = $("#graphic_tab");
    data.forEach(function(item){
        $(
            '<tr/>',
                {
            }).append($('<td/>', {
                text : item.id
            }))
            .append($('<td/>',{
                text : item.name
            }))
            .append($('<td/>',{
                text : item[site_type]
            }))
            .append($('<td/>',{
                text : item[sign_type]
            }))
            .append($('<td/>',{
                text : item.area
            }))
            .append($('<td/>',{
                text : item[longi_lati_tude]
            }))
            .append($('<td/>',{
                text : item.description
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