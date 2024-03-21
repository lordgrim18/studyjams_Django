## Welcome to Day 1 of the Django Study Jams Session

### How to follow along
- Look at the commit history of this repository to see the changes made in each step. 
- Only the commands used in the command line will be mentioned in the README.
- The code changes will be visible in the commit history.
- The commit messages are self-explanatory and will help you understand the changes made in each step.
- The commit messages follows the flow and can therefore be used as a guide to follow along.

### Today's Agenda:
- Introduction to Django
- Creating a virtual environment
- Setting up Django
- Creating a Django Project
- Creating a Django App
- Connecting Django App to Project
- Templates and Views
- Understanding Django Project Structure

### Introduction to Django
Django is a high-level Python web framework that encourages rapid development and clean, pragmatic design. It is a free and open-source web framework, written in Python, which follows the model-view-template architectural pattern. Django's primary goal is to ease the creation of complex, database-driven websites. 
Django follows a batteries-included philosophy. It provides almost everything developers might want to do "out of the box". This includes an ORM system, admin panel, URL routing, template engine, and more.

### Creating a virtual environment
A virtual environment is a self-contained directory that contains a Python installation for a particular version of Python, plus a number of additional packages. It allows you to work on a specific project without worrying about the dependencies of other projects. To create a virtual environment, you can use the following command:
```
python -m venv myenv
```
Here, `myenv` is the name of the virtual environment. You can replace it with any name you like.

Note: for linux users, you may need to use `python3` instead of `python` in the command.

#### Activating the virtual environment
To activate the virtual environment, you can use the following command:
for windows:
```
myenv\Scripts\activate
```
for linux:
```
source myenv/bin/activate
```
Here, `myenv` is the name of the virtual environment. You can replace it with the name of your virtual environment.

Note:
Sometimes virtual environment may not be deactivated automatically.
To deactivate the virtual environment, you can use the following command:
```
deactivate
```

### Setting up Django
To install Django, you can use the following command:
```
pip install django
```

### Creating a Django Project
To create a Django project, you can use the following command:
```
django-admin startproject studyjams_django
```
Here, `studyjams_django` is the name of the project. You can replace it with any name you like.

### Creating a Django App
To create a Django app, you can use the following command:
```
python manage.py startapp base
```
Here, `base` is the name of the app. You can replace it with any name you like.

### Understanding Django Project Structure
A Django project is a collection of settings, apps, and other configurations that when combined together make a web application. A Django project can contain multiple apps. Each app is a web application that does something – e.g., a blog system, a database of public records, a small poll app, etc.

The Django project structure is as follows:
```
base/
    __init__.py
    admin.py
    apps.py
    migrations/
        __init__.py
    models.py
    templates/
        base/
            blog.html
            home.html
    tests.py
    urls.py
    views.py
studyjams_django/
    __init__.py
    asgi.py
    settings.py
    urls.py
    wsgi.py
templates/
    main.html
    navbar.html
manage.py
```

- `manage.py`: A command-line utility that lets you interact with this Django project in various ways.
-
- `studyjams_django/`: The outer `studyjams_django/` directory is just a container for your project. Its name doesn’t matter to Django; you can rename it to anything you like.
- `studyjams_django/__init__.py`: An empty file that tells Python that this directory should be considered a Python package.
- `studyjams_django/asgi.py`: An entry-point for ASGI-compatible web servers to serve your project.
- `studyjams_django/settings.py`: Settings/configuration for this Django project.
- `studyjams_django/urls.py`: The URL declarations for this Django project; a “table of contents” of your Django-powered site.
- `studyjams_django/wsgi.py`: An entry-point for WSGI-compatible web servers to serve your project.
- 
- `base/`: The inner `base/` directory is the actual Python package for your project. Its name is the Python package name you’ll need to use to import anything inside it.
- `base/__init__.py`: An empty file that tells Python that this directory should be considered a Python package.
- `base/admin.py`: This file is used to register your models to the Django admin application.
- `base/apps.py`: This file is used to define the configuration of the app.
- `base/migrations/`: This directory contains all the migrations files for the app.
- `base/models.py`: This file is used to define the database models for the app.
- `base/templates/`: This directory contains all the HTML templates for the app.
- `base/tests.py`: This file is used to write tests for the app.
- `base/urls.py`: This file is used to define the URL patterns for the app.
- `base/views.py`: This file is used to define the views for the app.
- 
- `templates/`: This directory contains all the HTML templates for the project.

### Conclusion
In this session, we learned about Django, created a virtual environment, set up Django, created a Django project, created a Django app, and understood the Django project structure.
