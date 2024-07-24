from .base import *

DEBUG = True

ALLOWED_HOSTS = ['*']

DATABASES = {

    "default": {        
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.environ.get('POSTGRES_DB'),
        "USER": os.environ.get('POSTGRES_USER'),
        "PASSWORD": os.environ.get('POSTGRES_PASSWORD'),
        "HOST": 'db',
        "PORT": os.environ.get('POSTGRES_PORT'),
    },
    'test': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}