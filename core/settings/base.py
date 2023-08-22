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
    },
    'root': {
        'handlers': ['console'],
        'level': 'INFO',
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


MEDIA_ROOT =  os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'
 
STATICFILES_FINDERS = (
 
'django.contrib.staticfiles.finders.FileSystemFinder',
 
'django.contrib.staticfiles.finders.AppDirectoriesFinder',
 
)

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'


REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.JSONRenderer',
    )
}