from .base import *
from opentelemetry.instrumentation.django import DjangoInstrumentor
from opentelemetry.instrumentation.psycopg2 import Psycopg2Instrumentor
from opentelemetry.instrumentation.requests import RequestsInstrumentor
import uptrace

SECRET_KEY = os.environ.get('SECRET_KEY_LOCAL')

DEBUG = True

ALLOWED_HOSTS = ['*']

DATABASES = {

    "default": {        
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.environ.get('POSTGRES_DB_LOCAL'),
        "USER": os.environ.get('POSTGRES_USER_LOCAL'),
        "PASSWORD": os.environ.get('POSTGRES_PASSWORD_LOCAL'),
        "HOST": 'db',
        "PORT": os.environ.get('POSTGRES_PORT'),
    }
}


# Configure Uptrace with environment-specific settings
uptrace.configure_opentelemetry(
    dsn=os.environ.get('UPTRACE_DSN'),
    service_name="power_labs",
    service_version="v1.0.0",
    deployment_environment='STAGING'
)

# Instrument Django and psycopg2 with OpenTelemetry
DjangoInstrumentor().instrument()
Psycopg2Instrumentor().instrument()
