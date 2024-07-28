"""
Django settings for power_labs project.

Generated by 'django-admin startproject' using Django 5.0.7.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""

from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECRET_KEY = os.environ.get('SECRET_KEY')

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'django_filters',

    'xauth',
    'xuser',
    'sensors'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'power_labs.middlewares.LoggingMiddleware',
    'power_labs.middlewares.Handle404ErrorsMiddleware',
    'power_labs.middlewares.Handle403ErrorsMiddleware',
    'power_labs.middlewares.Handle500ErrorsMiddleware'
]

ROOT_URLCONF = 'power_labs.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'power_labs.wsgi.application'


# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'CET'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "xauth.auth_backends.JWTAuthentication",
    ),
    'DEFAULT_FILTER_BACKENDS': ['django_filters.rest_framework.DjangoFilterBackend'],
    'DEFAULT_PAGINATION_CLASS': 'power_labs.pagination.PowerLabsPagination',
    'PAGE_SIZE': 10
}

APPEND_SLASH = False

AUTH_USER_MODEL = "xuser.CustomUser"


# OpenTelemetry configuration
OTEL_SERVICE_NAME = 'power_labs'

OTEL_TRACES_EXPORTER = 'otlp'
OTEL_LOGS_EXPORTER = 'otlp'  
# OTEL_METRICS_EXPORTER = 'oltp'  # Optional for metrics

OTEL_PYTHON_LOGGING_AUTO_INSTRUMENTATION_ENABLED = True
OTEL_PYTHON_LOG_CORRELATION = True
OTEL_PYTHON_LOG_LEVEL = 'info'

# Enable gzip compression.
OTEL_EXPORTER_OTLP_COMPRESSION = 'gzip'
# Prefer delta temporality.
OTEL_EXPORTER_OTLP_METRICS_TEMPORALITY_PREFERENCE = 'DELTA'  # Optional for metrics

# Uptrace Login
OTEL_EXPORTER_OTLP_HEADERS = f"uptrace-dsn={os.environ.get('UPTRACE_DSN')}" 

# Export endpoint, local Uptrace instance
OTEL_EXPORTER_OTLP_ENDPOINT = '127.0.0.1:14317'
OTEL_EXPORTER_OTLP_INSECURE = False 
