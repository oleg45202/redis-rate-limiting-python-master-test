import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'configuration.settings')

app = get_wsgi_application()

os.system("python manage.py collectstatic")
os.system("python manage.py runserver")