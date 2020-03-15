# !/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Core app module for abstract models"""

from django.db import models


class AbstractBasicModel(models.Model):
    """
    Holds basic fields for any models
    """
    created_at = models.DateTimeField(blank=True, auto_now_add=True, verbose_name='Created At')
    updated_at = models.DateTimeField(blank=True, auto_now=True, verbose_name='Updated At')

    class Meta:
        abstract = True
