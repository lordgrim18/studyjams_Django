from django.contrib import admin

# Register your models here.

from .models import Blog, Topic, Comment, User

admin.site.register(User)

admin.site.register(Blog)
admin.site.register(Topic)
admin.site.register(Comment)