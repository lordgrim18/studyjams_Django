from django.shortcuts import render

blogs = [
    {'id':1, 'name': 'introduction to python'},
    {'id':2, 'name': 'introduction to django'},
    {'id':3, 'name': 'introduction to flask'},
]



def home(request):
    context = {'blogs': blogs}
    return render(request, 'home.html', context)

def blog(request):
    return render(request, 'blog.html')