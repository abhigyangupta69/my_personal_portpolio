from django.shortcuts import render,get_object_or_404
from .models import Blog

# Create your views here.

def home_blog(request):
    # blogs = Blog.objects.all()
    blogs = Blog.objects.order_by('-date')[:2] ##Starting 2 blogs show
    return render(request,'blog/home_blog.html',{'blog':blogs})


def details(request,blog_id):
    blog=get_object_or_404(Blog,pk=blog_id)###if Blog Id not available in Db Will give 404 error
    return render(request,'blog/detail.html',{'blog':blog})