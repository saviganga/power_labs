"""
WSGI config for power_labs project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

if os.environ["ENVIRONMENT"] == "LOCAL":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "power_labs.settings.local")
elif os.environ["ENVIRONMENT"] == "CLOUD":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "power_labs.settings.cloud")

application = get_wsgi_application()