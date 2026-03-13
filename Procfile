web: python manage.py collectstatic --noinput && python manage.py migrate && gunicorn mysite.wsgi --log-file - --workers 2
