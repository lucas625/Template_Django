# !/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Project wsgi module."""

import os

from django.core.wsgi import get_wsgi_application


os.environ.setdefault(
    'DJANGO_SETTINGS_MODULE',
    'Template_Django.settings'
)

application = get_wsgi_application()
