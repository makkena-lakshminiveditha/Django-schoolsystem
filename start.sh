python manage.py collectstatic --noinput
python manage.py migrate --noinput
gunicorn School_management_system.wsgi:application --biond 0.0.0.0 $PORT