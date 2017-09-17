#!/bin/sh
set -e

# change into app directory (start.sh can not be there because of volume)
cd /usr/src/tuiuiu.io

# run django setup commands if enabled
if [ "$DJANGO_MIGRATE" == "true" ]; then
    echo 'migrate'
    python manage.py migrate --noinput
fi
if [ "$LOAD_INITIAL_DATA" == "true" ]; then
    echo 'load_initial_data'
    python manage.py load_initial_data
fi
if [ "$DJANGO_COLLECTSTATIC" == "true" ]; then
    echo 'collectstatic'
    python manage.py collectstatic --noinput
fi

# start gunicorn
echo 'start gunicorn...'
if [ "$GUNICORN_RELOAD" == "true" ]; then
    echo 'with --reload'
    gunicorn -c /etc/gunicorn/gunicorn.conf --reload app.wsgi
else
    echo 'without --reload'
    gunicorn -c /etc/gunicorn/gunicorn.conf app.wsgi
fi
