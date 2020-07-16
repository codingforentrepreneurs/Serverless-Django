## Standard migration

```
python manage.py migrate
```

## Different Settings Module
```
python manage.py migrate --settings serverless_django.settings.production
```
> old version: `python manage.py migrate --settings:serverless_django.prod_settings`


## Using Environment Variables
```
DJANGO_SETTINGS_MODULE=serverless_django.settings.production python manage.py migrate
```