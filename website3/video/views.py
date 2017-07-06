from django.http import Http404
from django.shortcuts import render
from .models import Video

def index(request):
    all_category = Video.objects.all()
    context = { 'all_category' : all_category,
    }
    return render(request,'video/index.html',context)

def detail(request, category_id):
   try :
       category = Video.objects.get(pk=category_id)
   except Video.DoesNotExist:
       raise Http404("Category dose not exist")
   return render(request, 'video/detail.html', { 'category' : category, })