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


## WSGI Server

#### Gunicorn (preferred)
```
gunicorn serverless_django.wsgiwsgi:application
```

```
gunicorn serverless_django.wsgi:application --env DJANGO_SETTINGS_MODULE=serverless_django.settings.production
```


#### Waitress

```
waitress-serve serverless_django.wsgi:application
```

```
DJANGO_SETTINGS_MODULE=serverless_django.settings.production waitress-serve --port=8000 serverless_django.wsgi:application
```

