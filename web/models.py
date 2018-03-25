from __future__ import unicode_literals
from django.db import models

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
    parent_map=models.ForeignKey(Map,on_delete=models.CASCADE,default=0)

class User(models.Model):
    name=models.CharField(max_length=20)
    password=models.CharField(max_length=20)

    def __str__(self):
    # 在Python3中使用 def __str__(self):
        return self.name

