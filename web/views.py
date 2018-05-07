


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
from django.forms.models import model_to_dict
from django.core.serializers.json import DjangoJSONEncoder
from django.http import HttpResponse, JsonResponse
User = get_user_model()
from web.ImageryServer import DB_Workshop
from web.ImageryServer import ImagePubMan
import urllib.request
from web.ImageryServer import ImagePreprogress
# Create your views here.
##################################################
#from web.models import Map
###############################################



def index(request):
    return render(request,
                  template_name='index.html')

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


def register(request):
    return render(request,
                  template_name='register.html')

def add_account(request):
    return render(request,
                  template_name='am_add_Account.html')

#@login_required(login_url='/login/')
#@permission_required('resource_permission',login_url='/index/',raise_exception=True)
def account_inquiry(request):
    return render(request,
                  template_name='am_account_Inquiry.html')

def info_revise(request):
    username= request.session['username']
    user=User.objects.get(username=username)
    user=model_to_dict(user)
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

def user_center(request):
    return render(request,
                  template_name='view_user_center.html')

def account_management(request):
    return render(request,
                  template_name='view_account_management.html')
users_temp=User.objects.all()
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
    users_temp=User.objects.all()
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

def move_out(request):
    return render(request,
                  template_name='view_demolition.html')

def ib_plotting(request):
    return render(request,
                  template_name='ib_plotting.html')

def offence_build(request):
    return render(request,
                  template_name='view_illegal_building.html')

def general_survey(request):
    return render(request,
                  template_name='view_general_survey.html')

def graphic_look(request):
    return render(request,
                  template_name='gs_show_list.html')

def resource_management(request):
    return render(request,
                  template_name='view_resource_management.html')

def default(request):
    return render(request,
                  template_name='default_municipal.html')

def resource_search(request):
    response=urllib.request.urlopen('http://172.20.53.158:8089/deliver_map/')
    sourceMaps=json.loads(json.loads(response.read().decode('utf-8'))['d_maps'])
    localMapsTemp = Map.objects.all()
    localMaps={}
    #localGloID=[]
    if localMapsTemp:
        for i in range(len(localMapsTemp)):
            localMaps[localMapsTemp[i].GlobeID]=model_to_dict(localMapsTemp[i])
            #localGloID.append(localMaps[i]['GlobeID'])
    if sourceMaps:
        return render(request, 'rm_resource_search.html', {'sourceMaps': json.dumps(sourceMaps, cls=DjangoJSONEncoder),
                      'localMaps':json.dumps(localMaps,cls=DjangoJSONEncoder)})
                      #'localGloID':json.dumps(localGloID,cls=DjangoJSONEncoder)})
    else:
        return render(request, 'rm_resource_search.html', {'message': '查找结果为空！'})


def ib_event_management(request):
    ib_draws=GraphicLabel.objects.filter(graphiclabel='违建')
    d_ib_draws = {}
    for i in range(len(ib_draws)):
        d_ib_draws[i] = model_to_dict(ib_draws[i])
    return render(request,'ib_event_management.html',{'d_ib_draws': json.dumps(d_ib_draws, cls=DjangoJSONEncoder)})

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
        return render(request, 'index_new.html', {'message1': '登录成功'})

    else:
       return render(request, 'login.html', {'message1': '用户名或密码错误'})


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
    user=model_to_dict(user)
    user_permissions = []
    for j in range(len(user['user_permissions'])):
        tmp = user['user_permissions'][j].name
        user_permissions.append(tmp)

    return HttpResponse(json.dumps({"new_permissions":user_permissions}))

#@login_required
#@permission_required('user_management',raise_exception=True)
def _account_inquiry(request):
    message = request.POST.get('message',False)
    query_method=request.POST.get('query_method',False)
    #method_dic={'1':'username','2':'department_name','3':'phone','4':'contact_usr'}
    #method=method_dic[query_method]
    users_temp=[]
    if query_method == '1':
     users_temp=User.objects.filter(username=message)
    if query_method == '2':
     users_temp=User.objects.filter(department_name=message)
    if query_method == '3':
     users_temp=User.objects.filter(phone=message)
    if query_method == '4':
     users_temp=User.objects.filter(contact_usr=message)
    users = {}
    for i in range(len(users_temp)):
          users[i] = model_to_dict(users_temp[i])
    if users:
          return render(request,'am_account_Inquiry.html',locals())
    else:
          return render(request,'am_account_Inquiry.html',{'message1':'查找结果为空！'})



#@login_required
#@permission_required('user_management',raise_exception=True)
def _permissions_query(request):
    message = request.POST.get('message',False)
    query_method = request.POST.get('query_method', False)
    users_temp = []
    if query_method == '1':
        users_temp = User.objects.filter(username=message)
    if query_method == '2':
        users_temp = User.objects.filter(department_name=message)
    if query_method == '3':
        users_temp = User.objects.filter(phone=message)
    if query_method == '4':
        users_temp = User.objects.filter(contact_usr=message)
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
    return render(request,'am_permissions_management.html',{'userid':id,'isactive':is_active})


def save_draw(request):
    raw_dic = request.POST.get('coordi', False)
    name = request.POST.get('name', False)
    graphictype = request.POST.get('grahpictype', False)
    graphiclabel = request.POST.get('grahpiclabel', False)
    discrib = request.POST.get('discrib', False)
    square = request.POST.get('square', 0)
    coordinate = request.POST.get('coordinate', False)

    coordis=raw_dic.replace(",",";").split(";")
    coordis_num=[float(c) for c in coordis]
    coordis_list=[coordis_num[i:i+2] for i in range(0,len(coordis_num),2)]
    jsonstr={'type':'Feature','geometry':{'type':'Polygon','coordinates':[coordis_list]},'properties':{'id':0}}
    jsondata=json.dumps(jsonstr)
    draw_obj = GraphicLabel.objects.create(name=name,context=jsondata,graphictype=graphictype,graphiclabel=graphiclabel,graphic_provide=request.user,discrib=discrib)
    draw_obj.save()
    return render(request,'map_geo.html',{'message':'success'})


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
    return JsonResponse({'drawinfo':draw})


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

def test(request):
    ImagePreprogress.preprogress()
    #DB_Workshop.saveImage('/media/zhou/文档/yaogan')



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
    graphictype=request.GET.get('query_type',False)
    createtime=request.GET.get('query_time',False)
    graphicaddress=request.GET.get('query_address',False)
    ib_draws = GraphicLabel.objects.all()
    if(graphictype):
        ib_draws=GraphicLabel.objects.filter(graphictype=graphictype)
    if(name):
        ib_draws=GraphicLabel.objects.filter(name=name)
    if(graphicaddress):
        ib_draws=GraphicLabel.objects.filter(graphicaddress=graphicaddress)
    if(createtime):
        ib_draws=GraphicLabel.objects.filter(createtime=createtime)
    d_ib_draws = {}
    for i in range(len(ib_draws)):
        d_ib_draws[i] = model_to_dict(ib_draws[i])
    return JsonResponse({'data': d_ib_draws})
