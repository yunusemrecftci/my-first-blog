
from django.urls import path
from .views import *
from django.urls import re_path

app_name = 'post'
urlpatterns = [
    
    path('create/',post_create,name='create'),
    re_path(r'^(?P<slug>[\w-]+)/$', post_detail, name = 'detail' ),
    re_path(r'^(?P<slug>[\w-]+)/update/$', post_update, name = 'update' ),
    re_path(r'^(?P<slug>[\w-]+)/detele/$', post_detele, name = 'detele' ),
    
]
 