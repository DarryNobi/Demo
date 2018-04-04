


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
from django.contrib import auth
from web.models import Myuser
from django.forms.models import model_to_dict
User = get_user_model()
# Create your views here.



def index(request):
    return render(request,
                  template_name='index.html')

def loadmap(request):
    return render(request,
                  template_name='map.html')

def login(request):
    return render(request,
                  template_name='login.html')


def register(request):
    return render(request,
                  template_name='register.html')

def add_account(request):
    return render(request,
                  template_name='add_Account.html')

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
                  template_name='Permissions-query.html')

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
        if user.is_active:
            auth.login(request, user)
            return render(request, 'index.html', {'message1': '登录成功'})
        else:
            return render(request, 'login.html', {'message1': '用户被禁用'})
    else:
       return render(request, 'login.html', {'message1': '用户不存在'})


@login_required
def logout(request):
    logout(request)

@login_required
@permission_required('user_management',raise_exception=True)
def password_reset(request):
    username = request.POST.get("username",False)
    old_password = request.POST.get("password",False)
    new_password = request.POST.get("new_password",False)
    user = auth.authenticate(username=username, password=old_password)
    if user is not None:
        user.set_password(new_password)
        user.save()
        return render(request, {'message': '修改成功！'})
    else:
        return render(request, {'message': '用户名或密码错误!'})


@login_required
@permission_required('user_management',raise_exception=True)
def usr_info_revise(request):
    username = request.POST.get("username",False)
    department_name = request.POST.get("department_name",False)
    contact_usr = request.POST.get("contact_usr",False)
    phone = request.POST.get("phone",False)
    user = User.objects.filter(username=username)
    if user:
        user.department_name=department_name
        user.contact_usr=contact_usr
        user.phone=phone
        user.save()
        return render(request,{'message':'修改成功！'})
    else:
        return render(request,{'message':'用户不存在！'})

@login_required
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

@login_required
@permission_required('user_management',raise_exception=True)
def delete_usr(request):
    username = request.POST.get('username',False)
    user=User.objects.filter(username=username)
    user.delete()
    return render(request,{'message':'删除成功！'})

@login_required
@permission_required('user_management',raise_exception=True)
def enable_usr(request):
    username = request.POST.get('username',False)
    user=User.objects.filter(username=username)
    user.is_active=True
    user.save()
    return render(request,{'message':'启用成功！'})

@login_required
@permission_required('user_management',raise_exception=True)
def unenable_usr(request):
    username = request.POST.get('username',False)
    user=User.objects.filter(username=username)
    user.is_active=False
    user.save()
    return render(request,{'message':'禁用成功！'})


@login_required

def permission_revise(request):
    userid = request.POST.get("userid", False)
    check_box = request.POST.getlist('check_box',False)
    user = User.objects.filter(id=userid)
    dictionary={'user_management','ibuild_management','delimotion_management','recource_management'}
    for i in range(0,4):
       if 'i' in check_box:
        user.user_permissions.add(dictionary[i])
       elif user.has_perm(dictionary[i]):
        user.user_permissions.delete(dictionary[i])

    return render(request,{'message':'修改成功！'})


def _account_inquiry(request):
    username = request.POST.get('username',False)
    users=Myuser.objects.filter(username=username)
    myuser=Myuser.objects.filter(username=username)
    if users:
        return render(request,locals())
    else:
        return render(request,{'message':'没有找到该用户！'})