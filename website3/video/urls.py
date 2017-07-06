from django.conf.urls import  url
from . import views

app_name = 'video'

urlpatterns = [
   # /video/
   url(r'^$',views.index, name = 'index'),
   # /video/categoryid
   url(r'^(?P<category_id>[0-9]+)/$',views.detail, name= 'detail'),
   ]
