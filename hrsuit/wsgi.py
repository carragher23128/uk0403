"""
WSGI config for hrsuit project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/howto/deployment/wsgi/
"""

import os
import sys
from django.core.wsgi import get_wsgi_application

#追加
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/..')
sys.path.append('/home/venv/hrsuit')
sys.path.append("/path/to/projecthome/")
sys.path.append("/path/to/projecthome/hrsuit")

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "hrsuit.settings")
application = get_wsgi_application()
app = application
