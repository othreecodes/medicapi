release: python manage.py migrate --no-input
web: gunicorn medicapi.wsgi:application -