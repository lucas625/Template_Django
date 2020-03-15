# !/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Core app urls module"""

from django.urls import path
from django.conf.urls import include
from rest_framework import routers

from core.viewsset.template_model_viewset import TemplateModelViewSet


# it provide an easy way of automatically determining the URL conf
ROUTER = routers.DefaultRouter()
ROUTER.register('template-model', TemplateModelViewSet)

app_name = 'core'

urlpatterns = [  # pylint: disable=invalid-name
    path('api/', include(ROUTER.urls)),
]
