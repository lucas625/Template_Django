# !/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Module for testing core app rest API"""

from django.test import TestCase


class APIRestGetTestCase(TestCase):
    """Test cases for rest API get"""

    @classmethod
    def setUpTestData(cls):
        super(APIRestGetTestCase, cls)
        cls._url = '/api/'

    def test_get_student_rest_api_page_status_ok(self):
        """Checks the status of a get request to the API page."""
        response = self.client.get(self._url)
        self.assertEqual(response.status_code, 200)
