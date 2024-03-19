from django.shortcuts import render

from .models import Blog, Comment


def home(request):
    blogs = Blog.objects.all()
    context = {
        'blogs': blogs
    }
    return render(request, 'base/home.html', context)

def blog(request, pk):
    blog = Blog.objects.get(id=pk)
    comments = Comment.objects.filter(blog=blog)  # Filter comments for this blog
    context = {
        'blog': blog,
        'comments': comments,  # Add comments to the context
    }
    return render(request, 'base/blog.html', context)