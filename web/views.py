


from __future__ import unicode_literals
from django.shortcuts import render
from django.http import  HttpResponse
from web.models import User


# Create your views here.


def index(request):
    return render(request,
                  template_name='index.html')
def login(request):
    return render(request,
                  template_name='login.html')
def register(request):
    return render(request,
                  template_name='register.html')

def save_graphic(request):
    if request.method == "POST":
        data = request.POST.get('graphic')


def regist_db(request):


        username = request.POST.get("username", False)
        password = request.POST.get("password1", False)
        user=User.objects.create(name=username,password=password)
        user.save()

        return render(request, 'register.html',{'message1':'注册成功','message2':'立即登录 '})

def login_check(request):
    username = request.POST.get("username", False)
    password= request.POST.get("password", False)

    user = User.objects.filter(name=username,password=password)

    if user:
        return render(request,'index.html')
    else:
        return render(request,'login.html',{'message':'登录失败'})

def username_check(request):
    username = request.POST.get("username", False)
    user = User.objects.filter(name=username)

    if user:
        return render(request, True)
    else:
        return render(request, False)



