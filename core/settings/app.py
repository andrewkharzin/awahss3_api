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
    'simple_history',
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
    'django_nextjs',

]
    
PROJECT_APPS = [
    'apps.users',
    'apps.directory.airlines',
    'apps.flights',
    'apps.companies',
    'apps.schedules',

]


INSTALLED_APPS = DJANGO_APPS + THIRDPARTY_APPS + PROJECT_APPS