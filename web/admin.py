from __future__ import unicode_literals
from django.contrib import admin

# Register your models here.

from web.models import *
admin.site.register(BookInfo)
admin.site.register(HeroInfo)