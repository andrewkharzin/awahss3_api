
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

# CORS_ORIGIN_WHITELIST = [
#     "http://localhost:3000", 
#     "http://127.0.0.1:8000",
#     "http://192.168.1.121:3000",
#     ]

CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOW_CREDENTIALS = True

IMPORT_EXPORT_USE_TRANSACTIONS = True


CORS_ALLOWED_ORIGINS = [
    "http://127.0.0.1:3000",
    "http://localhost:3000",
    "http://192.168.1.121:3000"
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

JWT_AUTH = {
    'JWT_VERIFY_EXPIRATION': True,
    'JWT_ALLOW_REFRESH': True,
    'JWT_AUTH_HEADER_PREFIX': 'Bearer',
    'JWT_PAYLOAD_HANDLER': 'graphql_jwt.utils.jwt_payload',
    'JWT_PAYLOAD_GET_USER_ID_HANDLER': 'graphql_jwt.utils.jwt_get_user_id_from_payload_handler',
    'JWT_RESPONSE_PAYLOAD_HANDLER': 'myproject.schema.jwt_response_payload_handler',
    'JWT_SECRET_KEY': 'mysecretkey',
}


# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

