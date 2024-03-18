from django.contrib import admin
from django.urls import path
from django.http import HttpResponse

def home(request):
    return HttpResponse('Hello, Django!')

def blog(request):
    return HttpResponse('This is the blog.')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    path('blog/', blog),
]
