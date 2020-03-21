# !/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Module for testing template model rest API."""

from django.test import TestCase

from core.models.template_model import TemplateModel
from core.tests import helper


class TemplateModelRestPostTestCase(TestCase):
    """Test cases for Template model rest API post."""

    @classmethod
    def setUpTestData(cls):
        super(TemplateModelRestPostTestCase, cls)
        cls._url = '/api/template-model/'
        cls._template_model_values = helper.build_template_model_dict_data()

    def test_post_template_model_status_ok(self):
        """Checks the status of a post request to the template model's page."""
        response = self.client.post(self._url, self._template_model_values)
        self.assertEqual(response.status_code, 201)

    def test_post_template_model_content_type(self):
        """Checks the content type of a post request to the template model's page."""
        response = self.client.post(self._url, self._template_model_values)
        self.assertEqual(response['content-type'], 'application/json')


class TemplateModelRestGetTestCase(TestCase):
    """Test cases for Template model rest API get."""

    @classmethod
    def setUpTestData(cls):
        super(TemplateModelRestGetTestCase, cls)
        cls._url = '/api/template-model/'
        cls._template_model_values = helper.build_template_model_dict_data()
        cls._template_model = TemplateModel(**cls._template_model_values)
        cls._template_model.save()

    def test_get_template_model_rest_api_page_status_ok(self):
        """Checks the status of a get request to the template model's page."""
        response = self.client.get(self._url)
        self.assertEqual(response.status_code, 200)

    def test_get_template_model_content_type(self):
        """Checks the content type of a get request to the template model's page."""
        response = self.client.get(self._url)
        self.assertEqual(response['content-type'], 'application/json')

    def test_get_existent_template_model_status_ok(self):
        """Checks the status of a get request of a template model to the template model's page."""
        response = self.client.get('{}{}/'.format(self._url, str(self._template_model.id)))
        self.assertEqual(response.status_code, 200)

    def test_get_nonexistent_template_model_status_fail(self):
        """
        Checks the status of a get request of an nonexistent template model to
         the template model's page.
        """
        response = self.client.get('{}{}/'.format(self._url, str(self._template_model.id + 1)))
        self.assertEqual(response.status_code, 404)
