# !/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Core app module for template model serializer."""

from rest_framework import serializers

from core.models import TemplateModel


class TemplateModelSerializer(serializers.ModelSerializer):
    """
    Serializes the Template model.
    """

    class Meta:
        """Template Model Serializer meta class."""
        model = TemplateModel
        fields = '__all__'
