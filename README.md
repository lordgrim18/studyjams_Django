## Welcome to Day 2 of the Django Study Jams Session

### How to follow along
- Look at the commit history of this repository to see the changes made in each step. 
- Only the commands used in the command line will be mentioned in the README.
- The code changes will be visible in the commit history.
- The commit messages are self-explanatory and will help you understand the changes made in each step.
- The commit messages follows the flow and can therefore be used as a guide to follow along.

### Today's Agenda:
- Migrations in Django
- Models in Django
- Django Admin
- Registering Models in Django Admin
- Creating Superuser
- Django ORM

### What is Django ORM?
Django ORM is a powerful tool that maps the objects of our application to the database. It is a high-level abstraction that allows us to define our data models in Python and then automatically translates them into SQL queries. It is a powerful tool that allows us to interact with the database without writing SQL queries.

### Migrations in Django?
Migrations are a way to propagate changes you make to your models (adding a field, deleting a model, etc.) into your database schema. They’re designed to be mostly automatic, but you’ll need to know when to make migrations, when to run them, and the common problems you might run into.

- make migrations: It is used to create new migrations based on the changes you have made to your models.
- migrate: It is used to apply the migrations to the database.

The migration files for each app live in a “migrations” directory inside of that app, and are designed to be committed to, and distributed as part of, its codebase.

The command to make migrations is:
```python manage.py makemigrations```

The command to apply the migrations to the database is:
```python manage.py migrate```

Note: You should run the make migrations command whenever you make changes to your models.
    : Initial migrations are created when you start a new project and even when you create a new app. Run the migrate command to apply the initial migrations to the database.

### Models in Django
A model is the single, definitive source of information about your data. It contains the essential fields and behaviors of the data you’re storing. Generally, each model maps to a single database table.

### Django Admin
Django Admin is a powerful tool that allows us to manage our application data. It is a built-in app that allows us to create, read, update and delete the data in our application. It is a powerful tool that allows us to manage our application data without writing any code.

### Registering Models in Django Admin
To manage the data of a model in Django Admin, we need to register the model in the admin.py file of the app. We can do this by importing the model and then registering it using the admin.site.register() method.

### Creating Superuser
A superuser is a user with all permissions. We can create a superuser using the createsuperuser command. The command will prompt you to enter a username, email and password for the superuser.

The command to create a superuser is
```python manage.py createsuperuser```

### Conclusion
In this session, we learned about migrations in Django, models in Django, Django Admin, registering models in Django Admin, creating a superuser and Django ORM. We also learned how to use the Django ORM to interact with the database without writing SQL queries.
