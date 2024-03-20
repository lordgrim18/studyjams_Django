from django.shortcuts import render, redirect

from .models import Blog, Comment
from .forms import BlogForm


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

def createBlog(request):
    form = BlogForm()
    if request.method == 'POST':
        form = BlogForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'form': form}
    return render(request, 'base/blog_form.html', context)