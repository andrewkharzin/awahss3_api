from .base import *
import dj_database_url

DATABASES = {
    'default': dj_database_url.parse(os.environ.get('DATABASE_URL'), conn_max_age=600),
}


# DATABASES = {
#     # 'default': {
#     #     'ENGINE': 'django.db.backends.postgresql',
#     #     'NAME': 'awahss_db1',
#     #     'USER': 'postgres',
#     #     'PASSWORD': '19831112',
#     #     'HOST': 'skyjets.space',
#     #     'PORT': '5432',
#     # },
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
#     # 'default': {
#     #     'ENGINE': 'django.db.backends.mysql',
#     #     'NAME': 'andrewkharzin_awahss_db',
#     #     'USER': 'andrewkharzin_awahss_db',
#     #     'PASSWORD': 'Awahss_db19831112',
#     #     'HOST': '31.172.71.224',
#     #     'PORT': '3306',
#     #     'OPTIONS': {
#     #         'init_command': "SET sql_mode='STRICT_TRANS_TABLES'"
#     #     }
#     # }
# }
