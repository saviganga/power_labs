from .base import *
from opentelemetry.instrumentation.django import DjangoInstrumentor
from opentelemetry.instrumentation.psycopg2 import Psycopg2Instrumentor
from opentelemetry.instrumentation.requests import RequestsInstrumentor
import uptrace

SECRET_KEY = os.environ.get('SECRET_KEY')

DEBUG = False

ALLOWED_HOSTS = ['*']

DATABASES = {

    "default": {        
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.environ.get('POSTGRES_DB'),
        "USER": os.environ.get('POSTGRES_USER'),
        "PASSWORD": os.environ.get('POSTGRES_PASSWORD'),
        "HOST": os.environ.get('DB_HOST'),
        "PORT": os.environ.get('POSTGRES_PORT'),
    }
}


# Configure Uptrace with environment-specific settings
uptrace.configure_opentelemetry(
    dsn=os.environ.get('UPTRACE_DSN'),
    service_name="power_labs",
    service_version="v1.0.0",
    deployment_environment='CLOUD'
)

# Instrument Django and psycopg2 with OpenTelemetry
DjangoInstrumentor().instrument()
Psycopg2Instrumentor().instrument()
