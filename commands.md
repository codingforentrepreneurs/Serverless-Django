# Reference Commands
Reference commands that we use in this project.

## Django Settings

#### Standard migration
```
python manage.py migrate
```

#### Different Settings Module
```
python manage.py migrate --settings serverless_django.settings.production

python manage.py runserver --settings serverless_django.settings.production
```

#### Using Environment Variables
```
DJANGO_SETTINGS_MODULE=serverless_django.settings.production python manage.py migrate
```