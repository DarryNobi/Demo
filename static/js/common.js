function open_link(frame_name,url){
    document.getElementById(frame_name).src = url;
}

function open_link(url){
    document.getElementById("context_container").src = url;
}

function open_municipal_management(url){
    document.getElementById("municipal_container").src = url;
}

function open_demolition(url){
    document.getElementById("demolition_container").src = url;
}

function open_illegal_building(url){
    document.getElementById("illegal_building_container").src = url;
}

function open_resource_management(url){
    document.getElementById("resource_management_container").src = url;
}

function open_general_survey(url){
    document.getElementById("general_survey_container").src = url;
}

function open_account_management(url){
    document.getElementById("account_management_container").src = url;
}

function open_user_center(url){
    document.getElementById("user_center_container").src = url;
}

function open_download(url){
    window.parent.parent.document.getElementById("municipal_container").src = url;
}
