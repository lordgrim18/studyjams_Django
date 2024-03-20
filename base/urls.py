from django.urls import path

from . import views

urlpatterns = [
    # path('', views.home, name='home'),
    path('', views.Home.as_view(), name='home'),
    # path('blog/<str:pk>/', views.blog, name='blog'),
    path('blog/<str:pk>/', views.BlogDetail.as_view(), name='blog'),

    # path('create-blog/', views.createBlog, name='create-blog'),
    path('create-blog/', views.CreateBlog.as_view(), name='create-blog'),
    # path('update-blog/<str:pk>/', views.updateBlog, name='update-blog'),
    path('update-blog/<str:pk>/', views.UpdateBlog.as_view(), name='update-blog'),
    # path('delete-blog/<str:pk>/', views.deleteBlog, name='delete-blog'),
    path('delete-blog/<str:pk>/', views.DeleteBlog.as_view(), name='delete-blog'),
    
]
