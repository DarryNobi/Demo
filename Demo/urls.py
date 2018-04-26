
"""Demo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import  url
from web import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'^index/', views.index),
    url(r'^default/', views.default),
    url(r'^index_new/', views.index_new),
    url(r'^register/', views.register),
    url(r'^login/', views.login),
    url(r'^map/', views.loadmap),
    url(r'^add_account/', views.add_account),
    url(r'^password_revise/', views.password_revise),
    url(r'^permissions_query/', views.permissions_query),
    url(r'^account_inquiry/', views.account_inquiry),
    url(r'^roller_shutters/', views.roller_shutters),
    url(r'^info_revise/', views.info_revise),
    url(r'^authority_management/', views.authority_management),
    url(r'^ranging/', views.ranging),
    url(r'^home/', views.home),
    url(r'^move_out/', views.move_out),
    url(r'^move_compare/', views.move_compare),
    url(r'^offence_build/', views.offence_build),
    url(r'^resource_search/', views.resource_search),

##########################################################################

    url(r'^is_authenticated/', views.is_authenticated),
    url(r'^delete_usr/', views. delete_usr),
    url(r'^register_db/', views.regist_db),
    url(r'^login_check/', views.login_check),
    url(r'^password_reset/', views.password_reset),
    url(r'^usr_info_revise/', views.usr_info_revise),
    url(r'^logout/', views.mylogout),
    url(r'^permission_revise/', views.permission_revise),
    url(r'^add_usr/', views.add_usr),
    url(r'^password_reset/', views.password_reset),
    url(r'^_account_inquiry/', views._account_inquiry),
    url(r'^check_username/', views.check_username),
    url(r'^_permissions_query/',views._permissions_query),
    url(r'^status_revise/', views.status_revise),
    url(r'^save_draw/', views.save_draw),
    url(r'^load_all_draw/', views.load_all_draw),
    url(r'^query_draw/', views.query_draw),
    url(r'^delete_draw/', views.delete_draw),
]

urlpatterns += staticfiles_urlpatterns()