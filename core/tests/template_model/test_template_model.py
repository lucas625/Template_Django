# !/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Module for testing template model."""

from django.test import TestCase

from core.models.template_model import TemplateModel
from core.tests import helper


class TemplateModelMethodTestCase(TestCase):
    """Test cases for Template model methods."""

    @classmethod
    def setUpTestData(cls):
        super(TemplateModelMethodTestCase, cls)
        template_model_values = helper.build_template_model_dict_data()
        cls._template_model = TemplateModel(**template_model_values)
        cls._template_model.save()

    def test_template_model_str_method(self):
        """Checks if a template model's str method is equivalent to its full name."""
        self.assertEqual(self._template_model.full_name, str(self._template_model))
