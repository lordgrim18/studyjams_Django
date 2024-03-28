from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from .models import Blog, User

class BlogForm(ModelForm):
    class Meta:
        model = Blog
        fields = '__all__'
        exclude = ['author']

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['name', 'email', 'about']

class MyUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['name', 'email', 'password1', 'password2']