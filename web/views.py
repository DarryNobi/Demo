


from __future__ import unicode_literals
from django.shortcuts import render
from django.http import  HttpResponse
import logging
# Create your views here.
logger = logging.getLogger('django')
logging.info('hello!')

def index(request):
    logger.info('hi you!')
    logging.info('hello!')
    return render(request,
                  template_name='index.html')

def save_graphic(request):
    if request.method == "POST":
        data = request.POST.get('graphic')
        logger.info(data)

def check_user(request):
    username=request.get['username']
    password=request.get['password']
