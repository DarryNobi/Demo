from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth import get_user_model
from django.conf import settings
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.


class Map(models.Model):
    Maptype=(
        ('1','多光谱'),
        ('2','全色彩'),
        ('3','混合')
    )
    Maptype=models.CharField(max_length=8,choices=Maptype)
    name=models.CharField(max_length=10)
    longitude=models.FloatField()
    latitude=models.FloatField()
    width=models.BigIntegerField()
    height=models.BigIntegerField()
    filepath=models.FileField()
    cut_row=models.IntegerField()
    cut_col=models.IntegerField()
    gen_date=models.DateTimeField()
    folder=models.FilePathField()

class SliceMap(models.Model):
    index_raw=models.IntegerField()
    index_col=models.IntegerField()
    filepath=models.FileField()
    parent_map=models.ForeignKey(Map,on_delete=models.CASCADE)

class Myuser(AbstractUser):
    email=models.CharField(max_length=40,blank=True)
    first_name = models.CharField(max_length=20,default='a',blank=True)
    last_name = models.CharField(max_length=20, default='b',blank=True)
    is_active=models.BooleanField(default=True,blank=True)
    is_staff=models.BooleanField(default=True,blank=True)
    is_superuser=models.BooleanField(default=False,blank=True)
    date_joined=models.DateTimeField(blank=True,default=timezone.now)
    department_name=models.CharField(max_length=20,default='a',blank=True)
    contact_usr=models.CharField(max_length=20,blank=True,default='a')
    phone=models.CharField(max_length=20,blank=True,default='123')


    class Meta():
        permissions = (
            ("user_management", "用户管理"),
            ("ibuild_management", "违建管理"),
            ("demolition_management", "拆迁管理"),
            ("recource_management", "资源管理")
        )
#    def __str__(self):
#    # 在Python3中使用 def __str__(self):
#        return self.name

class GraphicLabel(models.Model):
    GraphicType=(
        ('1','建筑'),
        ('2','道路'),
        ('3','河流')
    )
    GraphicLabel = (
        ('1', '拆迁'),
        ('2', '违建')
    )
    name = models.CharField(max_length=16)
    grahpictype = models.CharField(max_length=4,choices=GraphicType)#地物类型如建筑、森林、河流
    grahpiclabel = models.CharField(max_length=4,choices=GraphicLabel)#标注类型如拆迁、违建
    context = models.TextField()#坐标数据
    discrib = models.TextField()
    square = models.FloatField(default=0)
    graphic_provide= models.ForeignKey(Myuser,on_delete=models.CASCADE,blank=True)
    coordinate_x = models.FloatField(default=0)
    coordinate_y = models.FloatField(default=0)