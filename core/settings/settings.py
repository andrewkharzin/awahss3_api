
from .base import *
from .middleware import *
from .templates import *
from .db import *


# If the environment variable DJANGO_ENV is set to 'production', use the production settings
if os.environ.get('DJANGO_ENV') == 'production':
    from .production import *

# Otherwise, use the local settings
else:
    from .local import *
    
SECRET_KEY = 'django-insecure-1z6wx-nv6wi&8v=@)_jzj1w!5b_p+i^ncfi4dfr5u%_m&ktwx^'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

CORS_ORIGIN_WHITELIST = [
    "http://localhost:3000", 
    "http://127.0.0.1:8000",
    "http://127.0.0.1:8888",
    ]

CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOW_CREDENTIALS = True

IMPORT_EXPORT_USE_TRANSACTIONS = True


CORS_ALLOWED_ORIGINS = [
    "http://127.0.0.1:8888",
    "http://localhost:8888",
]

CORS_EXPOSE_HEADERS = ['Content-Type', 'X-CSRFToken']

CSRF_TRUSTED_ORIGINS = [
    "http://andrewkharzin-psychic-fortnight-pwrrgjrj64c6pj6-8000.preview.app.github.dev",
    "https://andrewkharzin-psychic-fortnight-pwrrgjrj64c6pj6-8000.preview.app.github.dev",
]
# Application definition

INSTALLED_APPS = INSTALLED_APPS
MIDDLEWARE = MIDDLEWARE
TEMPLATES = TEMPLATES
DATABASES = DATABASES
 




WSGI_APPLICATION = 'core.wsgi.application'

ROOT_URLCONF = 'core.urls'


AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

