import os

# all base settings for Django
from .base import *

from .installed import *

ALLOWED_HOSTS = ['serverless-django-un3qlwrkgq-uw.a.run.app']
DEBUG = False

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get("SECRET_KEY", '+sn5=%=4*+da^!dfsr5q%k$cqeov_@352ihfvzzxoc6$9o!x91d')


print("Using production")
# Database

HOME_PAGE_MSG = f"Hello World. This Is Production."


DB_USER_UN = os.environ.get("DB_USER_UN", "")
DB_USER_PW = os.environ.get("DB_USER_PW", 'abc')
DB_NAME = os.environ.get("DB_NAME", "production")
INSTANCE_CONNECTION_NAME = os.environ.get('INSTANCE_CONNECTION_NAME')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': DB_NAME,
        'USER': DB_USER_UN,
        "PASSWORD": DB_USER_PW,
        "HOST": f'/cloudsql/{INSTANCE_CONNECTION_NAME}',
    }
}