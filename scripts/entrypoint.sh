#!/bin/bash

/usr/local/bin/gunicorn serverless_django.wsgi:application --bind "0.0.0.0:$PORT" --env DJANGO_SETTINGS_MODULE=serverless_django.settings.production