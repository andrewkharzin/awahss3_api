from .base import *
import secrets
import string

# Генерация нового безопасного SECRET_KEY


def generate_secret_key(length=50):
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(secrets.choice(characters) for _ in range(length))


# Используйте новый SECRET_KEY в настройках Django
SECRET_KEY = generate_secret_key()

DEBUG = True

DATABASES = {
    # 'default': {
    #     'ENGINE': 'django.db.backends.postgresql',
    #     'NAME': 'awahss_db1',
    #     'USER': 'postgres',
    #     'PASSWORD': '19831112',
    #     'HOST': 'skyjets.space',
    #     'PORT': '5432',
    # },
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
    # 'default': {
    #     'ENGINE': 'django.db.backends.mysql',
    #     'NAME': 'andrewkharzin_awahss_db',
    #     'USER': 'andrewkharzin_awahss_db',
    #     'PASSWORD': 'Awahss_db19831112',
    #     'HOST': '31.172.71.224',
    #     'PORT': '3306',
    #     'OPTIONS': {
    #         'init_command': "SET sql_mode='STRICT_TRANS_TABLES'"
    #     }
    # }
}
