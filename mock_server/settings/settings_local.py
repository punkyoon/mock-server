from .settings_base import *


DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(os.path.dirname(PROJECT_DIR), 'db.sqlite3'),
    }
}
