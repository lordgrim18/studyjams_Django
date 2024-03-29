## Welcome to the deployment day of Django Study Jams Session 

We will be deploying our Django project to [pythonanywhere](https://www.pythonanywhere.com/).

### Setting up your local repository before deployment:

1. In your local repository, create a .env file in the root directory.
2. This file will contain the keys and sensitive content that will be used in our project.
3. Add a .gitignore file in the root directory.
4. Add the following lines to the .gitignore file:
    ```bash
    __pycache__
    *.pyc
    *.pyo
    *.pyd

    .env
    venv/
    ```
    Here we are ignoring the .env file and the virtual environment folder which is named venv.
    If you have named your virtual environment folder something else, replace venv with the name of your virtual environment folder.
    This is done to prevent the sensitive content in the .env file from being uploaded to the repository.
5. Add a .env.sample file in the root directory.
   This file will contain the varible names of the keys and sensitive content that will be used in our project. And what the values of these variables should be.
6. Make sure that your virtual environment is activated.
7. Install the python decouple package used to access the .env content using the following command:
    ```bash
    pip install python-decouple
    ```
8. Update the settings.py file using python-decouple
9. Obtain the requirements of the project, ie the packages used in the project.
    ```bash
    pip freeze > requirements.txt
    ```
10. Now push the project into your github repository.

### Steps to deploy the project:

1. Create an account on [pythonanywhere](https://www.pythonanywhere.com/).
2. Go to the dashboard and under `New Console` press `$Bash`.
3. In the console that opens, type the following command to clone the repository:
    ```bash
    git clone <github repo link>
    ```
4. Create a virtual environment:
    ```bash
    python3 -m venv venv
    ```
    Note: pythonanywhere has only upto python 3.10
    Note: check if the virtual environment has been activated by looking at the terminal prompt. It should look like this:
    ```bash
    (venv) $
    ```
    If it is not activated, activate it using the following command:
    ```bash
    source venv/bin/activate
    ```
5. Install the requirements:
    ```bash
    pip install -r requirements.txt
    ```
6. In dashboard, go to `Web` and press `Add a new web app`.
    - The page shows data on domain names and such. Click on `Next`.
    - Select `Manual configuration` in the content that appears.
    - Select the version of Python you are using, here we earlier created a venv for python 3.10 and so we will use 3.10.

7. We appear at a Configuration page
    - Scroll down and under the Virtualenv section, click on the line `Enter path to a virtualenv, if desired`.
    - Type in the name of the virtual environment we created earlier, `venv` and click on the tick button.
    - We see the path to our virtual environment in the text box.
    - Sometimes the path is not correct, so we need to correct it by typing in the correct path.
    - If we followed the steps correctly, the path should be `/home/<username>/venv`.
8. Now in the same page under the Code section, click on the WSGI configuration file.
    - We see a code editor open up.
    - We can see a section titled Django in the code editor.
    - Delete all the other code in the file
    - Uncomment the code in the Django section. The code should look like this:
    ```python
        import os
        import sys

        path = '/home/<username>/studyjams_Django/studyjams_django'  # use your username, github repo name and project name 
        # here the github repo name is studyjams_Django, project name is studyjams_django, project name is the name of the folder in which the settings.py file is present 
        if path not in sys.path:
            sys.path.append(path)

        os.environ['DJANGO_SETTINGS_MODULE'] = 'studyjams_django.settings'

        from django.core.wsgi import get_wsgi_application
        application = get_wsgi_application()
    ```
    - Save the file and go back web tab.
9. Copy the domain name which will be in the format `<username>.pythonanywhere.com`.
    - Go to the File tab and, navigate to the settings.py file in the project folder.
    - Add the domain name to the `ALLOWED_HOSTS` list.
    - Make sure to add the domain name in the following format:
    ```python
    ALLOWED_HOSTS = ['<username>.pythonanywhere.com']
    ```
    - Save the file. 
10. Go back to the Web tab and click on the Reload button.
11. Go to the domain name and you should see the project deployed.