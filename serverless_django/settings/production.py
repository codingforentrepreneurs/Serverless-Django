import os

# all base settings for Django
from .base import *

from .installed import *

ALLOWED_HOSTS = ['*']
DEBUG = False

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get("SECRET_KEY", '+sn5=%=4*+da^!xvr5q%k$cqeov_@352ihfvzzxoc6$9o!x91d')


print("Using production")
# Database

HOME_PAGE_MSG = "Hello World. This Is Production"
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db_prod.sqlite3'),
    }
}