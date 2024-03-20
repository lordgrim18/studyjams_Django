from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('blog/<str:pk>/', views.blog, name='blog'),

    path('create-blog/', views.createBlog, name='create-blog'),
]
