from django.shortcuts import render


def home(request):
    return render(request, 'base/home.html')

def blog(request):
    return render(request, 'base/blog.html')