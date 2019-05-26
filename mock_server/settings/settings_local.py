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

SIMPLE_JWT = {'ACCESS_TOKEN_LIFETIME': timedelta(days=1), 'REFRESH_TOKEN_LIFETIME': timedelta(days=7), }
