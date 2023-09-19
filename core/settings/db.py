from .base import *
DATABASES = {
    # 'default': {
    #     'ENGINE': 'django.db.backends.postgresql',
    #     'NAME': 'awahss_db_test',
    #     'USER': 'postgres',
    #     'PASSWORD': '19831112',
    #     'HOST': 'localhost',
    #     'PORT': '5432',
    # },
    # 'default': {
    #     'ENGINE': 'django.db.backends.sqlite3',
    #     'NAME': BASE_DIR / 'db.sqlite3',
    # },
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'awahss_db',
        'USER': 'awahss',
        'PASSWORD': 'awahss_db19831112',
        'HOST': '31.172.71.224',
        'PORT': '3306',
        'OPTIONS': {
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'"
        }
    }
}

# CACHES = {
#     'default': {
#         'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
#         'LOCATION': '127.0.0.1:11211',
#     }
# }
