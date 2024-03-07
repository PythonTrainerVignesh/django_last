python -m venv c:\path\to\myenv
python -m venv c:\path\to\myenv

# This should be executed in the powershell (Admin)
Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy Unrestricted

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'website',
        'USER': 'root',
        'PASSWORD': 'pass1234',
        'DEFAULT-CHARACTER-SET': 'utf8',
    }
}

pip install django
pip install mysqlclient
django-admin
django-admin startproject website .
python manage.py
python manage.py runserver 
python manage.py runserver 80
python .\manage.py makemigrations
python .\manage.py migrate
python .\manage.py createsuperuser


auto_now_add = Creation Time
auto_now = Update Time


python .\manage.py makemigrations website
python .\manage.py migrate
