from .base import *


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config('DEBUG')
ALLOWED_HOSTS = ['*']

SITE_URL = 'http://localhost:8000'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': config('db_name'),
        'USER': config('db_user'),
        'PASSWORD': config('db_password'),
        'HOST': config('db_host'),
        'PORT': config('db_port'),
    }
}


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'