DJANGO_APPS = [
    'django.contrib.admin',
    "django.contrib.sites",
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

THIRDPARTY_APPS = [
    'djoser',
    'simple_history',
    'drf_spectacular',
    'drf_spectacular_sidecar',
    'mptt',
    'tinymce',
    'phone_field',
    'import_export',
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

AUTH_APPS = [
   'corsheaders',
   "apps.authentication",
   'rest_framework',
   'rest_framework_simplejwt',
   "rest_framework.authtoken",
   "allauth",
   "allauth.account",
   "allauth.socialaccount",
   "dj_rest_auth",
   "dj_rest_auth.registration",
]


INSTALLED_APPS = DJANGO_APPS + THIRDPARTY_APPS + PROJECT_APPS + AUTH_APPS