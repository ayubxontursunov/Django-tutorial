# Django Tutorial

<img src="https://www.djangoproject.com/s/img/logos/django-logo-negative.png" alt="Django Logo" width="150"/>

This repository contains code for a Django tutorial covering the basics of setting up a Django project, creating apps, defining models, views, and templates.

## Getting Started

1. Clone this repository.
2. Install Django (`pip install django`).
3. Navigate to the project directory.
4. Run the server (`python manage.py runserver`).
5. Visit [http://localhost:8000/](http://localhost:8000/) in your browser.

For more detailed instructions, refer to the [tutorial documentation](https://docs.djangoproject.com/en/stable/).

# Static Files in Django

<img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg" alt="Python Logo" width="50"/>

This repository demonstrates how to manage static files (CSS, JavaScript, images) in a Django project.

## Usage

1. Ensure Django is installed (`pip install django`).
2. Clone this repository.
3. Add your static files to the `static` directory.
4. Reference your static files in your Django templates using the `{% static %}` template tag.
5. Run the server (`python manage.py runserver`) and navigate to your app to see the static files in action.

For more information, consult the [Django documentation](https://docs.djangoproject.com/en/stable/howto/static-files/).

# Django Static Files Management

This repository provides a comprehensive guide on managing static files in Django projects. Ensure your web application looks stunning by effectively handling CSS, JavaScript, and image files.

## Commands Cheatsheet

Here's a handy list of commands to kickstart your Django project:

- Initialize a new Django project: `django-admin startproject monte .`
- Create a new app within your project: `py manage.py startapp shop`
- Apply initial migrations: `py manage.py migrate`
- Make model changes: `py manage.py makemigrations shop`
- Apply model changes to the database: `py manage.py migrate`
- Generate SQL for a migration: `py manage.py sqlmigrate shop 0001`
- Access Django shell for interactive development: `py manage.py shell`
- Create a superuser for administrative access: `py manage.py createsuperuser`

Remember to execute these commands in your terminal to streamline your development process.

For more detailed instructions on managing static files and exploring Django's capabilities, dive into the official Django documentation.
