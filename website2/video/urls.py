from django.conf.urls import  url
from . import views
urlpatterns = [
   # /video/
   url(r'^$',views.index, name = 'index'),
   #/video/1/
   url(r'^(?P<category_id>[0-9]+)/$',views.detail, name= 'detail'),

   ]
