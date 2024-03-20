from django.shortcuts import render, redirect

from .models import Blog, Comment
from .forms import BlogForm


def home(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    blogs = Blog.objects.filter(topic__name__icontains=q)
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

def updateBlog(request, pk):
    blog = Blog.objects.get(id=pk)
    form = BlogForm(instance=blog)

    if request.method == 'POST':
        form = BlogForm(request.POST, instance=blog)
        if form.is_valid():
            form.save()
            return redirect('home')
        
    context = {'form': form}
    return render(request, 'base/blog_form.html', context)

def deleteBlog(request, pk):
    blog = Blog.objects.get(id=pk)
    if request.method == 'POST':
        blog.delete()
        return redirect('home')
    context = {'obj': blog}
    return render(request, 'base/delete.html', context)