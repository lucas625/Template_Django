#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Module for core app viewset."""

from rest_framework import viewsets

from core.models import TemplateModel
from core.serializers.template_model_serializer import TemplateModelSerializer


class TemplateModelViewSet(viewsets.ModelViewSet):  # pylint: disable=too-many-ancestors
    """
    It provides end-points for CRUD the template model.
    """
    queryset = TemplateModel.objects.all()
    serializer_class = TemplateModelSerializer
