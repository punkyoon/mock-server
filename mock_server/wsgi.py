import os

from django.core.wsgi import get_wsgi_application


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mock_server.settings.settings_local')
application = get_wsgi_application()
