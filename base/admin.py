from django.contrib import admin

# Register your models here.

from .models import Blog, Topic, Comment

admin.site.register(Blog)
admin.site.register(Topic)
admin.site.register(Comment)