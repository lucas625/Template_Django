# !/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Core app template model module"""

from django.db import models

from core.models.abstract_model import AbstractBasicModel


models.CharField.register_lookup(models.functions.Length)

class TemplateModel(AbstractBasicModel):
    """
    Template Model
    """
    full_name = models.CharField(max_length=150, null=True, verbose_name='Name')

    def __str__(self):
        """
        :return str: template model name
        """
        return self.full_name

    class Meta:
        abstract = False
        constraints = [
            models.CheckConstraint(
                check=models.Q(full_name__length__lte=150),
                name='template-model-name-length'
            ),
        ]
