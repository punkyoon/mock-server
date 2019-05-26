from .settings_base import *

from datetime import timedelta


ALLOWED_HOSTS = ['*']

DEBUG = True

CORS_ORIGIN_WHITELIST = ('http://localhost:3000', 'https://localhost:3000', )

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(os.path.dirname(PROJECT_DIR), 'db.sqlite3'),
    }
}

JWT_AUTH = {'JWT_AUTH_HEADER_PREFIX': 'Bearer', 'JWT_EXPIRATION_DELTA': timedelta(days=1)}
