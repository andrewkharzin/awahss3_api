from .base import *

SECRET_KEY = 'your-secret-key'

DEBUG = False

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'mydatabase',
        'USER': 'mydatabaseuser',
        'PASSWORD': 'mypassword',
        'HOST': 'mydatabase.host.com',
        'PORT': '5432',
    }
}

ALLOWED_HOSTS = ['myapp.host.com']