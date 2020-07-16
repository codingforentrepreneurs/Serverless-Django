import os

# all base settings for Django
from .base import *

from .installed import *


HOME_PAGE_MSG = "Hello World. This Is Local"
print("Using local")
# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}