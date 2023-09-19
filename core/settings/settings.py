import os
from .base import *
from datetime import timedelta
from .middleware import *
from .templates import *
from .db import *
from pathlib import Path
from dotenv import load_dotenv 

# If the environment variable DJANGO_ENV is set to 'production', use the production settings
if os.environ.get('DJANGO_ENV') == 'production':
    from .production import *

# Otherwise, use the local settings
else:
    from .local import *

SECRET_KEY = os.getenv('SECRET_KEY')

load_dotenv(BASE_DIR / '.env')  # new


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.getenv('DEBUG', '0').lower() in ['true', 't', '1']

ALLOWED_HOSTS = os.getenv('ALLOWED_HOSTS').split(' ')

# CORS_ORIGIN_WHITELIST = [
#     "http://localhost:3000",
#     "http://127.0.0.1:8000",
#     "http://192.168.1.121:8000",
#     "http://192.168.1.138:3000",
#     ]

CORS_ORIGIN_ALLOW_ALL = False
CORS_ALLOW_CREDENTIALS = False

IMPORT_EXPORT_USE_TRANSACTIONS = True


# if DEBUG:
#     CORS_ALLOW_ALL_ORIGINS = True
# else:
#     CORS_ALLOWED_ORIGINS = [
#         "http://localhost:3000/",
#         "http://127.0.0.1:3000/",
#     ]

CORS_ALLOWED_ORIGINS = [
    "http://127.0.0.1:3000",
    "http://localhost:3000",
    "http://192.168.1.121:3000",
    "http://192.168.1.138:3000",
    "https://b40b-94-25-168-214.ngrok-free.app",

]
# CORS_EXPOSE_HEADERS = ['Content-Type', 'X-CSRFToken']

# CSRF_TRUSTED_ORIGINS = []
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

AUTHENTICATION_BACKENDS = [
    'graphql_jwt.backends.JSONWebTokenBackend',
    'django.contrib.auth.backends.ModelBackend',
]


SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(minutes=60),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=7),
    "ROTATE_REFRESH_TOKENS": False,
    "BLACKLIST_AFTER_ROTATION": False,
    "UPDATE_LAST_LOGIN": True,
    "SIGNING_KEY": "complexsigningkey",  # generate a key and replace me
    "ALGORITHM": "HS512",
}

SITE_ID = 1

ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_EMAIL_VERIFICATION = "none"


REST_AUTH = {
    "USE_JWT": True,
    "JWT_AUTH_HTTPONLY": False,
}

ELASTICSEARCH_DSL = {
    'default': {
        'hosts': 'localhost:9200',  # Adjust to your Elasticsearch server's address
    },
}

# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

DATA_UPLOAD_MAX_NUMBER_FIELDS = 25000
