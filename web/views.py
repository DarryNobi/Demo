


from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.contrib.auth import logout
from django.contrib.auth.decorators import permission_required
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Permission
from django.contrib import auth
from web.models import Map
import json
from django.core import serializers
from web.models import Myuser
from web.models import GraphicLabel
from web.models import AutoGraphicLabel
from django.forms.models import model_to_dict
from django.core.serializers.json import DjangoJSONEncoder
from django.http import HttpResponse, JsonResponse
User = get_user_model()
from web.ImageryServer import DB_Workshop
from web.ImageryServer import ImagePubMan
from web.ImageryServer import Auto_graphiclabel
import urllib.request
from django.db.models import Q
#from web.ImageryServer import ImagePre
# Create your views here.
##################################################
from web.models import Map
###############################################



def index(request):
    return render(request,
                  template_name='index.html')
def _resource_search(request):
    return render(request,
                  template_name='rm_resource_search.html')

def index_new(request):
    return render(request,
                  template_name='index_new.html')

@login_required(login_url='/login/')
def loadmap(request):
    return render(request,
                  template_name='map_geo.html')

def login(request):
    # if request.method == "POST":
    #    uf = User
    return render(request,
                  template_name='login.html')

def not_login(request):
    # if request.method == "POST":
    #    uf = User
    return render(request,
                  template_name='not_login.html')

def no_permissions(request):
    return render(request,
                  template_name='no_permissions.html')


def register(request):
    return render(request,
                  template_name='register.html')

def add_account(request):
    return render(request,
                  template_name='am_add_Account.html')

#@login_required(login_url='/login/')
#@permission_required('resource_permission',login_url='/index/',raise_exception=True)
def account_inquiry(request):
    users_temp=User.objects.all().order_by('-date_joined')
    users = {}
    count = 1
    for i in range(len(users_temp)):
        users[i] = model_to_dict(users_temp[i])
        users[i]["num"] = count
        count = count + 1
        if (users[i]["is_active"]):
            users[i]["is_active"] = "启用"
        else:
            users[i]["is_active"] = "禁用"
        user_permissions = []
        for j in range(len(users[i]['user_permissions'])):
            tmp = users[i]['user_permissions'][j].name
            user_permissions.append(tmp)
        users[i]['user_permissions'] = user_permissions
    return render(request, 'am_account_Inquiry.html', {'users': json.dumps(users, cls=DjangoJSONEncoder)})



def info_revise(request):
    username= request.session['username']
    user=User.objects.get(username=username)
    user=model_to_dict(user)
    user_permissions = []
    for j in range(len(user['user_permissions'])):
        tmp = user['user_permissions'][j].name
        user_permissions.append(tmp)
    user['user_permissions'] = user_permissions
    return render(request,'uc_info_revise.html',{'user':json.dumps(user,cls=DjangoJSONEncoder)})

def password_revise(request):
    return render(request,
                  template_name='uc_password_revise.html')

def permissions_query(request):
    return render(request,
                  template_name='am_permissions_query.html')

def ib_roller_shutters(request):
    return render(request,
                  template_name='ib_roller_shutters.html')
#####################################################
@login_required(login_url="/not_login/")
def user_center(request):
    return render(request,
                  template_name='view_user_center.html')
@login_required(login_url="/not_login/")
@permission_required('web.user_management',login_url='/no_permissions/')
def account_management(request):
    return render(request,
                  template_name='view_account_management.html')
@login_required(login_url="/not_login/")
@permission_required('web.demolition_management',login_url='/no_permissions/')
def move_out(request):
    return render(request,
                  template_name='view_demolition.html')

@login_required(login_url="/not_login/")
@permission_required('web.ibuild_management',login_url='/no_permissions/')
def offence_build(request):
    return render(request,
                  template_name='view_illegal_building.html')
@login_required(login_url="/not_login/")
@permission_required('web.recource_management',login_url='/no_permissions/')
def general_survey(request):
    return render(request,
                  template_name='view_general_survey.html')

@login_required(login_url="/not_login/")
@permission_required('web.recource_management',login_url='/no_permissions/')
def resource_management(request):
    return render(request,
                  template_name='view_resource_management.html')


def uploadImage(request):

    imageID=request.POST.get('ImageID',False)
    return HttpResponse(ImagePubMan.uploadImage(imageID))

def cancelPublish(request):
    imageID=request.POST.get('ImageID',False)
    return HttpResponse(ImagePubMan.cancelPublish(imageID))

def downloadImage(request):
    imageID=request.POST.get('ImageID',False)
    return HttpResponse(ImagePubMan.downloadImage(imageID))
def deleteImage(request):
    imageID=request.POST.get('ImageID',False)
    return HttpResponse(ImagePubMan.deleteImage(imageID))
#####################################################

def authority_management(request):
    users_temp=User.objects.all().order_by('-date_joined')
    d_users={}
    for i in range(len(users_temp)):
          d_users[i] = model_to_dict(users_temp[i])
          user_permissions = []
          for j in range(len(d_users[i]['user_permissions'])):
            tmp=d_users[i]['user_permissions'][j].name
            user_permissions.append(tmp)
          d_users[i]['user_permissions']=user_permissions
    if d_users:
          return render(request,'am_permissions_management.html',{'d_users':json.dumps(d_users,cls=DjangoJSONEncoder)})
    else:
          return render(request,'am_permissions_management.html',{'message':'查找结果为空！'})

def ranging(request):
    return render(request,
                  template_name='ranging.html')

def home_municipal(request):
    return render(request,
                  template_name='home_municipal.html')


def demolition_management(request):
    return render(request, 'de_management.html')

def ib_event_management(request):
    return render(request,'ib_event_management.html')


def demolition_compare(request):
    return render(request,
                  template_name='de_compare.html')

def demolition_plotting(request):
    id=request.GET.get('id',False)
    x=0;y=0;
    if id:
        draw=GraphicLabel.objects.get(id=id)
        x=draw.coordinate_x
        y=draw.coordinate_y
    return render(request,'de_plotting.html',{'x':x,'y':y})

def developing(request):
    return render(request,
                  template_name='developing.html')

def ib_plotting(request):
    id=request.GET.get('id',False)
    x=0.0;y=0.0;
    if id:
        draw=GraphicLabel.objects.get(id=id)
        x=draw.coordinate_x
        y=draw.coordinate_y
    return render(request,'ib_plotting.html',{'x':x,'y':y})


def graphic_look(request):
    return render(request,
                  template_name='gs_show_list.html')

def default(request):
    return render(request,
                  template_name='default_municipal.html')

def resource_search(request):
    response=urllib.request.urlopen('http://172.20.53.158:8089/deliver_map/')
    sourceMaps=json.loads(json.loads(response.read().decode('utf-8'))['d_maps'])
    maptype=request.GET.get('maptype',False)
    resultMaps={}
    if(maptype=="请选择卫星种类"):
        return JsonResponse({'sourceMaps': sourceMaps})
    else:
        for k,v in sourceMaps.items():
            if(v["satelite"]==maptype):
                resultMaps[k]=v
        sourceMaps=resultMaps
    # if sourceMaps:
    return JsonResponse({'sourceMaps': sourceMaps})
    # else:
    #     return JsonResponse({'sourceMaps': sourceMaps, "message": False})

def rm_show_map(request):
    id = request.GET.get('id', False)
    map=Map.objects.filter(GlobeID=id)
    if(map):
        d_map = {}
        for i in range(len(map)):
            d_map[i] = model_to_dict(map[i])
        return render(request,'rm_show_map.html',{'map':json.dumps(d_map,cls=DjangoJSONEncoder)})
    else:
        return JsonResponse({'error':1})


def gs_show_map(request):
    return render(request,
                  template_name='gs_show_map.html')
def gs_show_list(request):
    return render(request,
                  template_name='gs_show_list.html')

#########################################################################

def is_authenticated(request):
    if request.user.is_authenticated:
        return JsonResponse({'islogin':True,'username':request.user.username})
    else:
        return JsonResponse({'islogin': False})


def save_graphic(request):
    if request.method == "POST":
        data = request.POST.get('graphic')


def regist_db(request):
        username = request.POST.get("username", False)
        password = request.POST.get("password1", False)
        department_name = request.POST.get(" department_name", False)
        contact_usr = request.POST.get("contact_usr", False)
        phone= request.POST.get("phone", False)
        user = User.objects.create_user(username=username,password=password)
        user.save()

        return render(request, 'register.html',{'message1':'注册成功','message2':'立即登录 '})


def login_check(request):
    username = request.POST.get("username", False)
    password= request.POST.get("password", False)
    user = auth.authenticate(username=username, password=password)
    if user:
        request.session['username']=username
        auth.login(request, user)

        return JsonResponse({"status": True,'username':username})
    else:
        return JsonResponse({"status": False,'message':'用户名或密码错误'})


def mylogout(request):
    logout(request)
    return render(request,'index_new.html',{'islogin': False})

#@login_required
#@permission_required('user_management',raise_exception=True)
def password_reset(request):

    old_password = request.POST.get("old_password",False)
    new_password = request.POST.get("new_password1",False)
    if request.user.check_password(old_password):
        request.user.set_password(new_password)
        request.user.save()

        return render(request, 'uc_password_revise.html', {'message': '修改成功！'})
    else:
        return render(request, 'uc_password_revise.html',{'message': '用户名或密码错误!'})


#@login_required
#@permission_required('user_management',raise_exception=True)
def usr_info_revise(request):
    username = request.POST.get("username",False)
    department_name = request.POST.get("department_name",False)
    contact_usr = request.POST.get("contact_usr",False)
    phone = request.POST.get("phone",False)
    user = User.objects.get(username=username)
    if user:
        user.contact_usr=contact_usr
        user.department_name=department_name
        user.phone=phone
        user.save()
        return render(request,'uc_info_revise.html', {'message': '修改成功！'})

    else:
        return render(request,{'message':'用户不存在！'})

#@login_required
#@permission_required('user_management',raise_exception=True)
def add_usr(request):
    username = request.POST.get("username", False)
    password= request.POST.get("password1", False)
    department_name= request.POST.get("department_name", False)
    contact_usr= request.POST.get("contact_usr", False)
    phone= request.POST.get("phone", False)
    user = User.objects.create_user(username=username, password=password,department_name=department_name,contact_usr=contact_usr,phone=phone)
    user.save()
    return render(request,'am_add_Account.html',{'message':'添加成功'})

#@login_required
#@permission_required('user_management',raise_exception=True)
def delete_usr(request):
    username = request.POST.get('username',False)
    user=User.objects.filter(username=username)
    user.delete()
    return render(request,{'message':'删除成功！'})




#@login_required
#@permission_required('user_management',raise_exception=True)
def permission_revise(request):
    userid = request.POST.get("id", False)
    check_box = request.POST.get('permission_value',False)
    check_box=json.loads(check_box)
    user = User.objects.get(id=userid)
    user.user_permissions.clear()
    permission_dict={'1':'user_management','2':'ibuild_management','3':'demolition_management', '4':'recource_management'}
    for i in check_box:
       permission = Permission.objects.get(codename=permission_dict[i])
       user.user_permissions.add( permission )
    user.save()
    user=model_to_dict(user)
    user_permissions = []
    for j in range(len(user['user_permissions'])):
        tmp = user['user_permissions'][j].name
        user_permissions.append(tmp)
    user['user_permissions']= user_permissions
    return HttpResponse(json.dumps({"user":user},cls=DjangoJSONEncoder))

#@login_required
#@permission_required('user_management',raise_exception=True)
def _account_inquiry(request):
    message = request.POST.get('message',False)
    if message=='':
        users_temp = User.objects.all().order_by('-date_joined')
        users = {}
        count = 1
        for i in range(len(users_temp)):
            users[i] = model_to_dict(users_temp[i])
            users[i]["num"] = count
            count = count + 1
            if (users[i]["is_active"]):
                users[i]["is_active"] = "启用"
            else:
                users[i]["is_active"] = "禁用"
            user_permissions = []
            for j in range(len(users[i]['user_permissions'])):
                tmp = users[i]['user_permissions'][j].name
                user_permissions.append(tmp)
            users[i]['user_permissions'] = user_permissions
        return JsonResponse({"users": users, "status": True})
    else:
        users_temp=User.objects.filter(Q(username__contains=message)\
        |Q(phone__contains=message)|Q(department_name__contains=message)|Q(contact_usr__contains=message)).order_by('-date_joined')
        users = {}
        count=1
        for i in range(len(users_temp)):
              users[i] = model_to_dict(users_temp[i])
              users[i]["num"]=count
              count=count+1
              if(users[i]["is_active"]):
                  users[i]["is_active"]="启用"
              else:
                  users[i]["is_active"]="禁用"
              user_permissions=[]
              for j in range(len(users[i]['user_permissions'])):
                  tmp = users[i]['user_permissions'][j].name
                  user_permissions.append(tmp)
              users[i]['user_permissions'] = user_permissions
        if users:
              return JsonResponse({"users":users,"status":True})
        else:
              return JsonResponse({"message":"查找结果为空！","status":False})



#@login_required
#@permission_required('user_management',raise_exception=True)
def _permissions_query(request):
    message = request.POST.get('message',False)
    query_method = request.POST.get('query_method', False)
    users_temp = []
    if query_method == '1':
        users_temp = User.objects.filter(username=message)
    users={}
    for i in range(len(users_temp)):
       users[i]=model_to_dict(users_temp[i])
       user_permissions = []
       for j in range(len(users[i]['user_permissions'])):
           tmp = users[i]['user_permissions'][j].name
           user_permissions.append(tmp)
       users[i]['user_permissions'] = user_permissions
    if users:
        return render(request,'am_permissions_query.html',locals())
    else:
        return render(request,'am_permissions_query.html',{'message1':'查找结果为空！'})


def check_username(request):
    username = request.POST.get('username', False)
    user=User.objects.filter(username=username)
    if user:
        return HttpResponse("false")
    else:
        return HttpResponse("true")


def status_revise(request):
    #raw_dic=request.raw_post_data()
    #dic=json.loads(raw_dic,cls=DjangoJSONEncoder)
    is_active=request.POST.get('is_active', False)
    id=request.POST.get('id', False)
    user=User.objects.get(id=id)
    user.is_active=is_active
    user.save()
    return JsonResponse({"message":"success"})


def save_draw(request):
    graphic_provide=request.user.id
    raw_dic = request.POST.get('coordi', False)
    name = request.POST.get('name', False)
    graphictype = request.POST.get('graphictype', False)
    graphiclabel = request.POST.get('graphiclabel', False)
    discrib = request.POST.get('discrib', False)
    square = request.POST.get('square', 0)
    address= request.POST.get('address', '无')
    coordis=raw_dic.replace(",",";").split(";")
    coordis_num=[float(c) for c in coordis]
    coordis_list=[coordis_num[i:i+2] for i in range(0,len(coordis_num),2)]
    coordinate_x=coordis_list[0][0]
    coordinate_y=coordis_list[0][1]
    jsonstr={'type':'Feature','geometry':{'type':'Polygon','coordinates':[coordis_list]},'properties':{'id':0}}
    jsondata=json.dumps(jsonstr)
    draw_obj = GraphicLabel.objects.create(name=name,context=jsondata,graphictype=graphictype,graphiclabel=graphiclabel,graphic_provide=request.user,discrib=discrib,square=square,address=address,coordinate_x=coordinate_x,coordinate_y=coordinate_y)
    draw_obj.save()
    return HttpResponse("success")

    #return render(request,'map_geo.html',{'message':'success'})
    #return HttpResponse("success")


def update_draw(request):
    id= request.POST.get('id', False)
    name = request.POST.get('name', False)
    graphictype = request.POST.get('graphictype', False)
    graphiclabel = request.POST.get('graphiclabel', False)
    discrib = request.POST.get('discrib', False)
    address= request.POST.get('address', '无')
    draw_obj=GraphicLabel.objects.get(id=id)
    if draw_obj:
        draw_obj.name=name
        draw_obj.graphictype=graphictype
        draw_obj.graphiclabel=graphiclabel
        draw_obj.discrib=discrib
        draw_obj.address=address
        draw_obj.save()
        return HttpResponse("success")
    else:
        return HttpResponse("fail")


def load_all_draw(request):
    all_draws=GraphicLabel.objects.all()
    for draw in all_draws:
        json_context=json.loads(draw.context)
        json_context['properties']['id']=draw.id
        draw.context=json.dumps(json_context)

    all_draws_data = [draw.context for draw in all_draws]
    return JsonResponse({'all_draws':all_draws_data})


def query_draw(request):
    id = request.GET.get('id', False)
    draw=model_to_dict(GraphicLabel.objects.get(id=id))
    if draw:
        x=draw['graphictype']
        y=draw['graphiclabel']
        return JsonResponse({'drawinfo':draw})
    else:
        return JsonResponse({'drawinfo':''})


def _delete_draw(request):
    id = request.GET.get('id', False)
    draw=GraphicLabel.objects.get(id=id)
    draw.delete()
    return JsonResponse({'message':'success'})

def map_inquiry(request):
    maps_temp = Map.objects.all()
    d_maps = {}
    for i in range(len(maps_temp)):
        d_maps[i] = model_to_dict(maps_temp[i])
    if d_maps:
        return render(request, 'rm_resource_search.html', {'d_maps': json.dumps(d_maps, cls=DjangoJSONEncoder)})
    else:
        return render(request, 'rm_resource_search.html', {'message': '查找结果为空！'})

def _map_inquiry(request):
    maps_temp = Map.objects.all()
    d_maps = {}
    for i in range(len(maps_temp)):
        d_maps[i] = model_to_dict(maps_temp[i])
    if d_maps:
        return HttpResponse(json.dumps(d_maps, cls=DjangoJSONEncoder))
    else:
        return HttpResponse({'message': '查找结果为空！'})

def _autographiclabel_inquiry(request):
    graphictype=request.GET.get('type',False)
    if graphictype:
        autographiclabel_temp=AutoGraphicLabel.objects.filter(graphictype=graphictype)
        #autographiclabel_temp = AutoGraphicLabel.objects.all()
        d_autographiclabel = {}
        for i in range(len(autographiclabel_temp)):
            d_autographiclabel[i] = autographiclabel_temp[i].context
        if d_autographiclabel:
            return JsonResponse({'d_autographiclabel':d_autographiclabel})
        else:
            return HttpResponse({'message': '查找结果为空！'})
    else:
        return HttpResponse({'message': '查找结果为空！'})


def test(request):
    #ImagePre.preprogress()
    #DB_Workshop.saveImage('/media/zhou/文档/yaogan')
    Auto_graphiclabel.main()



def _gs_show_list(request):
    query_name = request.GET.get('query_name', '')
    query_type = request.GET.get('query_type', '')
    draws=GraphicLabel.objects.all()
    if(query_type):
        draws = draws.filter(grahpictype=query_type)
    if(query_name):
        draws=draws.filter(name=query_name)
    d_draws=[]
    for i in range(len(draws)):
        d_draws.append(model_to_dict(draws[i]))
    if(d_draws):
        return JsonResponse({'data':d_draws})
    else:
        return JsonResponse({'message': '查找结果为空！'})

def _ib_event_search(request):
    name=request.GET.get('query_name',False)
    graphiclabel=request.GET.get('query_type',False)
    createtime=request.GET.get('query_time',False)
    address=request.GET.get('query_address',False)
    kwargs = {}
    kwargs['graphiclabel__contains'] = "违建"
    if(graphiclabel):
        kwargs['graphiclabel'] = graphiclabel
    if(name):
        kwargs['name__contains'] = name
    if(address):
        kwargs['address__contains'] = address
    if(createtime):
        kwargs['createtime'] = createtime
    ib_draws = GraphicLabel.objects.filter(**kwargs).order_by('-createtime')

    d_ib_draws = {}
    for i in range(len(ib_draws)):
        d_ib_draws[i] = model_to_dict(ib_draws[i])
        id = d_ib_draws[i]["graphic_provide"]
        user = User.objects.get(id=id)
        d_ib_draws[i]["graphic_provide"] = user.username
    return JsonResponse({'d_ib_draws': d_ib_draws})


def _de_event_search(request):
    name = request.GET.get('query_name', False)
    graphiclabel = request.GET.get('query_type', False)
    createtime = request.GET.get('query_time', False)
    address = request.GET.get('query_address', False)
    kwargs = {}
    kwargs['graphiclabel__contains'] = "拆迁"
    if (graphiclabel):
        kwargs['graphiclabel'] = graphiclabel
    if (name):
        kwargs['name__contains'] = name
    if (address):
        kwargs['address__contains'] = address
    if (createtime):
        kwargs['createtime'] = createtime
    de_draws = GraphicLabel.objects.filter(**kwargs).order_by('-createtime')
    d_de_draws = {}
    for i in range(len(de_draws)):
        d_de_draws[i] = model_to_dict(de_draws[i])
        id = d_de_draws[i]["graphic_provide"]
        user = User.objects.get(id=id)
        d_de_draws[i]["graphic_provide"] = user.username
    return JsonResponse({'d_ib_draws': d_de_draws})

def login_page(request):
    return render(request,"index_new.html",{"status":True})


def new_password_reset(request):
    username=request.POST.get("username",False)
    user=User.objects.get(username=username)
    user.set_password("12345678")
    user.save()
    return HttpResponse("success")

def locate(request):
    location=request.POST.get("location",False)
    req = urllib2.Request(url)
    dic={"keyWord":location}
    response = urllib.request.urlopen("http://api.tianditu.com/geocoder?ds="+dic)
    real_location= json.loads(json.loads(response.read().decode('utf-8'))['location'])
    return JsonResponse({"location":real_location})


