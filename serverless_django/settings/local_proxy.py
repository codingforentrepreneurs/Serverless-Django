import os

# all base settings for Django
from .base import *

from .installed import *

HOME_PAGE_MSG = "Hello World. This Is a Local Proxy"
print("Using local proxy")
# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db_proxy.sqlite3'),
    }
}