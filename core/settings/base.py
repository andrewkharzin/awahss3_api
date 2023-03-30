import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent.parent
PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))

DJANGO_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

THIRDPARTY_APPS = [
    'djoser',
    'rest_framework',
    'rest_framework_simplejwt',
    'drf_spectacular',
    'drf_spectacular_sidecar',
    'mptt',
    'tinymce',
    'phone_field',
    'import_export',
    'corsheaders',
    "django_tables2",
    "graphene_django",
    'crispy_forms',
    'author',
    'channels',
    'django_bookmark_base',
    "taggit", 
    'dynamic_raw_id',
    'django_select2',
    'admin_auto_filters',

]
    
PROJECT_APPS = [
    'apps.directory.airlines',

]


INSTALLED_APPS = DJANGO_APPS + THIRDPARTY_APPS + PROJECT_APPS

GRAPHENE = {
  "SCHEMA": "graph.schema.schema",
}

TIME_ZONE = 'UTC'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


STATICFILES_DIRS = (
 
os.path.join(PROJECT_ROOT, 'assets'),
 
)

STATIC_URL = 'static/'

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')


STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static/staticfiles'),
)

MEDIA_ROOT =  os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'
 
STATICFILES_FINDERS = (
 
'django.contrib.staticfiles.finders.FileSystemFinder',
 
'django.contrib.staticfiles.finders.AppDirectoriesFinder',
 
)