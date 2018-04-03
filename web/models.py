from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser

# Create your models here.

class GraphicLabel(models.Model):
    GraphicType=(
        ('1','建筑'),
        ('2','道路'),
        ('3','河流')
    )
    name = models.CharField(max_length=16)
    grahpictype = models.CharField(max_length=4,choices=GraphicType)
    context = models.FileField()

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

class User(AbstractUser):
    first_name=models.CharField(max_length=20,default='a')
    last_name = models.CharField(max_length=20, defalut='b')
    
    department_name=models.CharField(max_length=20,null=True)
    contact_usr=models.CharField(max_length=20,null=True)
    phone=models.CharField(max_length=20,null=True)
    enable=models.BooleanField(default=True)

    class Meta:
        permissions = (
            ("user_management", "用户管理"),
            ("ibuild_management", "违建管理"),
            ("demolition_management", "拆迁管理"),
            ("recource_management", "资源管理")
        )
    def __str__(self):
    # 在Python3中使用 def __str__(self):
        return self.name

