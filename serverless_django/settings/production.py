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
DB_USER_UN = os.environ.get("DB_USER_UN", "")
HOME_PAGE_MSG = f"Hello World. This Is Production."

DB_USER_PW = os.environ.get("DB_USER_PW", 'abc')


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db_prod.sqlite3'),
    }
}