python manage.py collectstatic --noinput
python manage.py migrate --noinput
gunicorn School_management_system.wsgi:application --bind 0.0.0.0:10000
