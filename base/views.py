from django.shortcuts import render

from .models import Blog


def home(request):
    blogs = Blog.objects.all()
    context = {
        'blogs': blogs
    }
    return render(request, 'base/home.html', context)

def blog(request, pk):
    blog = Blog.objects.get(id=pk)
    context = {
        'blog': blog
    }
    return render(request, 'base/blog.html', context)