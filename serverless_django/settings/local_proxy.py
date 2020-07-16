import os

# all base settings for Django
from .base import *

from .installed import *

HOME_PAGE_MSG = "Hello World. This Is a Local Proxy"
print("Using local proxy")
# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': "local",
        'USER': "dblocaluser",
        "PASSWORD": "<your_pw>",
        "HOST": '127.0.0.1',
        "PORT": 6543,
    }
}