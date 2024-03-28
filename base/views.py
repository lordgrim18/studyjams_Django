from django.shortcuts import render, redirect
from django.db.models import Q
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

from .models import Blog, Comment
from .forms import BlogForm

#############################################
### function based views
#############################################

def home(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    blogs = Blog.objects.filter(
        Q(topic__name__icontains=q) | 
        Q(title__icontains=q) |
        Q(body__icontains=q)
        )

    context = {
            'blogs': blogs,
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

def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'User does not exist')
            return redirect('login')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Username or password is incorrect')
            return redirect('login')
    context = {}
    return render(request, 'base/login_register.html', context)

def logoutUser(request):
    logout(request)
    return redirect('login')








#############################################
### class based views
#############################################
# from django.views.generic import View
# class Home(View):
#     def get(self, request):
#         q = request.GET.get('q') if request.GET.get('q') != None else ''
#         blogs = Blog.objects.filter(
#             Q(topic__name__icontains=q) | 
#             Q(title__icontains=q) |
#             Q(body__icontains=q)
#             )
#         topics = Topic.objects.all()
#         blog_count = blogs.count()

#         context = {
#             'blogs': blogs,
#             'topics': topics,
#             'blog_count': blog_count,
#         }
#         return render(request, 'base/home.html', context)
    
# class BlogDetail(View):
#     def get(self, request, pk):
#         blog = Blog.objects.get(id=pk)
#         comments = Comment.objects.filter(blog=blog)  # Filter comments for this blog
#         context = {
#             'blog': blog,
#             'comments': comments,  # Add comments to the context
#         }
#         return render(request, 'base/blog.html', context)

# class CreateBlog(View):
#     def get(self, request):
#         form = BlogForm()
#         context = {'form': form}
#         return render(request, 'base/blog_form.html', context)

#     def post(self, request):
#         form = BlogForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('home')
#         context = {'form': form}
#         return render(request, 'base/blog_form.html', context)
    
# class UpdateBlog(View):
#     def get(self, request, pk):
#         blog = Blog.objects.get(id=pk)
#         form = BlogForm(instance=blog)
#         context = {'form': form}
#         return render(request, 'base/blog_form.html', context)

#     def post(self, request, pk):
#         blog = Blog.objects.get(id=pk)
#         form = BlogForm(request.POST, instance=blog)
#         if form.is_valid():
#             form.save()
#             return redirect('home')
#         context = {'form': form}
#         return render(request, 'base/blog_form.html', context)

# class DeleteBlog(View):
#     def get(self, request, pk):
#         blog = Blog.objects.get(id=pk)
#         context = {'obj': blog}
#         return render(request, 'base/delete.html', context)

#     def post(self, request, pk):
#         blog = Blog.objects.get(id=pk)
#         blog.delete()
#         return redirect('home')
    
##################################################
### class based views using specific views
##################################################

# from django.views.generic import DetailView, CreateView, UpdateView, DeleteView

# class BlogDetail(DetailView):
#     model = Blog
#     template_name = 'base/blog.html'

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         blog = self.get_object()
#         comments = Comment.objects.filter(blog=blog)  # Filter comments for this blog
#         context['comments'] = comments
#         return context

# class CreateBlog(CreateView):
#     model = Blog
#     form_class = BlogForm
#     template_name = 'base/blog_form.html'
#     success_url = '/'  # Redirect to home page after successful creation

# class UpdateBlog(UpdateView):
#     model = Blog
#     form_class = BlogForm
#     template_name = 'base/blog_form.html'
#     success_url = '/'  # Redirect to home page after successful update

# class DeleteBlog(DeleteView):
#     model = Blog
#     template_name = 'base/delete.html'
#     success_url = '/'  # Redirect to home page after successful deletion