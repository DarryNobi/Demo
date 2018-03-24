


from __future__ import unicode_literals
from django.shortcuts import render
from django.http import  HttpResponse

# Create your views here.


def index(request):
    return render(request,
                  template_name='index.html')

def save_graphic(request):
    if request.method == "POST":
        data = request.POST.get('graphic')

def check_user(request):
    username=request.get['username']
    password=request.get['password']
