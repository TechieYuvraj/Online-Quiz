"""
WSGI config for onlinequiz project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/wsgi/
"""

import os
import sys
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)

try:
    from django.core.wsgi import get_wsgi_application
except Exception as e:
    logging.error("Failed to import Django WSGI application: %s", e)
    sys.exit(1)

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'onlinequiz.settings')

try:
    application = get_wsgi_application()
except Exception as e:
    logging.error("Failed to get WSGI application: %s", e)
    sys.exit(1)

app = application
