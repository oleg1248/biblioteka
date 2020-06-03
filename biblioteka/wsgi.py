"""
WSGI config for biblioteka project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/wsgi/
"""
import logging
import os

from django.core.wsgi import get_wsgi_application

from dotenv import load_dotenv


# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'biblioteka.settings.local')
load_dotenv()
application = get_wsgi_application()
logger = logging.getLogger(__name__)
logger.propagate = True
