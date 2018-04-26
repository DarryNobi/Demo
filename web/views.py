


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
from web.ImageryServer import GS_Workshop
# Create your views here.



def index(request):
    return render(request,
                  template_name='index.html')

def loadmap(request):
    return render(request,
                  template_name='map_geo.html')

def login(request):
    return render(request,
                  template_name='login.html')


def register(request):
    return render(request,
                  template_name='register.html')

def add_account(request):
    return render(request,
                  template_name='add_Account.html')

#@login_required(login_url='/login/')
#@permission_required('resource_permission',login_url='/index/',raise_exception=True)
def account_inquiry(request):
    return render(request,
                  template_name='account_Inquiry.html')

def info_revise(request):
    return render(request,
                  template_name='info_revise.html')

def password_revise(request):
    return render(request,
                  template_name='password_revise.html')

def permissions_query(request):
    return render(request,
                  template_name='permissions_query.html')

def roller_shutters(request):
    return render(request,
                  template_name='roller_shutters.html')

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
          return render(request,'authorityManagement.html',{'d_users':json.dumps(d_users,cls=DjangoJSONEncoder)})
    else:
          return render(request,'authorityManagement.html',{'message':'查找结果为空！'})

def ranging(request):
    return render(request,
                  template_name='ranging.html')

def home(request):
    return render(request,
                  template_name='home.html')

def resource_search(request):
    return render(request,
                  template_name='resource_search.html')
#########################################################################

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
        return render(request, 'index.html', {'message1': '登录成功'})

    else:
       return render(request, 'login.html', {'message1': '用户名或密码错误'})


def mylogout(request):
    logout(request)
    return render(request,'login.html')

#@login_required
#@permission_required('user_management',raise_exception=True)
def password_reset(request):

    old_password = request.POST.get("old_password",False)
    new_password = request.POST.get("new_password1",False)
    if request.user.check_password(old_password):
        request.user.set_password(new_password)
        request.user.save()

        return render(request, 'password_revise.html', {'message': '修改成功！'})
    else:
        return render(request, 'password_revise.html',{'message': '用户名或密码错误!'})


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
        return render(request,'info_revise.html', {'message': '修改成功！'})

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
    return render(request,'add_Account.html',{'message':'添加成功'})

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
          return render(request,'account_Inquiry.html',locals())
    else:
          return render(request,'account_Inquiry.html',{'message1':'查找结果为空！'})



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
        return render(request,'permissions_query.html',locals())
    else:
        return render(request,'permissions_query.html',{'message1':'查找结果为空！'})

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
    return render(request,'authorityManagement.html',{'userid':id,'isactive':is_active})

def save_draw(request):
    raw_dic = request.POST.get('coordi', False)
    coordis=raw_dic.replace(",",";").split(";")
    coordis_num=[float(c) for c in coordis]
    coordis_list=[coordis_num[i:i+2] for i in range(0,len(coordis_num),2)]
    jsonstr={'type':'Feature','geometry':{'type':'Polygon','coordinates':[coordis_list]},'properties':{'name':'name'}}
    jsondata=json.dumps(jsonstr)

    draw_obj = GraphicLabel.objects.create(name='default',context=jsondata,grahpictype='1',grahpiclabel='1')
    draw_obj.save()
    return render(request,'map_geo.html',{'message':'success'})

def load_all_draw(request):
    all_draws=GraphicLabel.objects.all()
    all_draws_data = [draw.context for draw in all_draws]
    return JsonResponse({'all_draws':all_draws_data})


############################
def getPath(request):
    return render(request,
                  template_name='image_Upload.html')


def SqlTest(request):
    filepath = request.POST.get('filepath', False)
    DB_Workshop.saveImage(filepath)
    return render(request, 'toGeoServer.html')


def toGeoServer(request):
    GS_Workshop.uploadImage();
    return render(request, 'toGeoServer.html')

