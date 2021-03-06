# My Notes

## 1. Django project

In Django terminology, a "Django project" is composed of several site-level configuration files, along with one or more "apps" that you deploy to a web host to create a full web application. A Django project can contain multiple apps, each of which typically has an independent function in the project, and the same app can be in multiple Django projects. An app, for its part, is just a Python package that follows certain conventions that Django expects.

### Useful Commands

```bat
REM Create the Django project named "web_project"
django-admin startproject web_project .

REM Create an empty development database
python manage.py migrate

REM Start development server on default port (8000)
python manage.py runserver

REM Start development server specifying port number
python manage.py runserver 5000

REM Create a Django app named "hello"
python manage.py startapp hello
```

## 2. Django app

The command creates a folder called `hello` that contains a number of code files and one subfolder. Of these, you frequently work with `views.py` (that contains the functions that define pages in your web app) and `models.py` (that contains classes defining your data objects).

The `migrations` folder is used by Django's administrative utility to manage database versions as discussed later in this tutorial.

The `urls.py` file is where you specify patterns to route different URLs to their appropriate views.

There are also the files `apps.py` (app configuration), `admin.py `(for creating an administrative interface), and `tests.py` (for creating tests), which are not covered here.

### Useful Commands

```bat
REM Create a Django app named "hello"
python manage.py startapp hello
```

## 3. Other Useful Commands

```bat
REM Collect all the static files from your apps into a single folder
REM It's a very typical approach when deploying to production
python manage.py collectstatic

REM Generate scripts in the migrations folder that migrate the database from its current state to the new state.
python manage.py makemigrations

REM Apply the scripts to the actual database.
python manage.py migrate
```

## 4. VS Code Tips

[Create a project environment for the Django tutorial](https://code.visualstudio.com/docs/python/tutorial-django#_create-a-project-environment-for-the-django-tutorial)

[Create a code snippet](https://code.visualstudio.com/docs/python/tutorial-django#_create-a-code-snippet)


## 5. Hosting on Heroku
[Great tutorial from Real Python](https://realpython.com/django-hosting-on-heroku/)