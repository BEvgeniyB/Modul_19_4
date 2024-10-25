from lib2to3.fixes.fix_input import context

from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render
from  django.views.generic import TemplateView
from django.core.paginator import Paginator
from .models import *
# Create your views here.

# class Index(TemplateView):
#     template_name = "index.html"
quantity_page = 3
def Index(request:WSGIRequest):
    post = Post.objects.all().order_by('creation_data')

    quantity_page = request.GET.get('quantity_page')

    paginator = Paginator(post,per_page=quantity_page)
    page_number = request.GET.get('page',1)
    page_obj = paginator.get_page(page_number)
    context= {'quantity_page2':quantity_page,'page_obj':page_obj}
    return render(request,'pagination.html',context)

