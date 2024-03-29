import os
from pathlib import Path
from datetime import timedelta

from .app import *
# from .graphene import GRAPHENE

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent.parent
PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))


INSTALLED_APPS = INSTALLED_APPS
# GRAPHENE = GRAPHENE

AUTH_USER_MODEL = 'users.User'

GRAPHENE = {
    "SCHEMA": "graph.schema.schema",
}

STRAWBERRY_DJANGO = {
    "FIELD_DESCRIPTION_FROM_HELP_TEXT": True,
    "TYPE_DESCRIPTION_FROM_MODEL_DOCSTRING": True,
}

TIME_ZONE = 'UTC'


CELERY_BROKER_URL = 'redis://localhost:6379/0'
CELERY_BEAT_SCHEDULE = {
    'update_flight_info': {
        'task': 'apps.schedules.tasks.update_flight_info_task',
        'schedule': timedelta(minutes=15),  # Run every 15 minutes
    },
}


LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': 'app.log',  # Имя файла для логов
        },
    },
    'root': {
        'handlers': ['console', 'file'],
        'level': 'INFO',  # Уровень логирования для корневого логгера
    },
    'loggers': {
        'django': {
            'handlers': ['console', 'file'],
            'level': 'INFO',
            'propagate': True,
        },
        'your_app_name': {
            'handlers': ['console', 'file'],
            'level': 'DEBUG',  # Уровень логирования для вашего приложения
            'propagate': True,
        },
    },
}


DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


STATICFILES_DIRS = (

    os.path.join(PROJECT_ROOT, 'assets'),

)

STATIC_URL = 'static/'

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')


STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'frontend/client', 'public'),
)


MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

STATICFILES_FINDERS = (

    'django.contrib.staticfiles.finders.FileSystemFinder',

    'django.contrib.staticfiles.finders.AppDirectoriesFinder',

)

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# SECURE_HSTS_SECONDS = 31536000  # 1 year
# SECURE_HSTS_INCLUDE_SUBDOMAINS = True

SECURE_PROXY_SSL_HEADER = None

SESSION_COOKIE_SECURE = False
CSRF_COOKIE_SECURE = False
SESSION_COOKIE_HTTPONLY = False
SECURE_SSL_REDIRECT = False

# # Укажите путь к сертификату и ключу
# CERTIFICATE_PATH = '.cert.pem'
# PRIVATE_KEY_PATH = '.key.pem'

# CERTIFICATE_PATH = os.path.abspath(CERTIFICATE_PATH)
# PRIVATE_KEY_PATH = os.path.abspath(PRIVATE_KEY_PATH)


REST_FRAMEWORK = {
    'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "rest_framework_simplejwt.authentication.JWTAuthentication",

    ]
}
