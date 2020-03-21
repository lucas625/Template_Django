# !/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Module for testing template model CRUD."""

from sqlite3 import IntegrityError as Sqlite3IntegrityError
import datetime

import freezegun
from django.test import TestCase
from django.db.utils import IntegrityError as DjangoIntegrityError

from core.models.template_model import TemplateModel
from core.tests import helper


class TemplateModelUpdateTestCase(TestCase):
    """Test cases for Template model update."""

    @classmethod
    def setUpTestData(cls):
        super(TemplateModelUpdateTestCase, cls)
        cls._template_model_values = helper.build_template_model_dict_data()

    @freezegun.freeze_time('2020-03-10 00:00:00')
    def setUp(self):
        super(TemplateModelUpdateTestCase, self).setUp()
        self._template_model = TemplateModel(**self._template_model_values)
        self._template_model.save()

    @freezegun.freeze_time('2020-03-11 00:00:00')
    def test_update_template_model_created_at_auto_now_add(self):
        """
        Checks if a template model is updated with the correct created at based on auto now add.
        """
        self._template_model.save()

        self.assertEqual(
            datetime.datetime.strftime(self._template_model.created_at, '%Y-%m-%d %H:%M:%S'),
            '2020-03-10 00:00:00'
        )

    @freezegun.freeze_time('2020-03-11 00:00:00')
    def test_save_template_model_updated_at_auto_now_add(self):
        """Checks if a template model is saved with the correct updated at based on auto now."""
        self._template_model.save()

        self.assertEqual(
            datetime.datetime.strftime(self._template_model.updated_at, '%Y-%m-%d %H:%M:%S'),
            '2020-03-11 00:00:00'
        )


class TemplateModelSaveTestCase(TestCase):
    """Test cases for Template model save."""

    @classmethod
    def setUpTestData(cls):
        super(TemplateModelSaveTestCase, cls)
        cls._template_model_values = helper.build_template_model_dict_data()

    def test_save_template_model(self):
        """Checks if a template model was saved."""
        template_model = TemplateModel(**self._template_model_values)
        template_model.save()
        self.assertTrue(template_model.id)

    def test_save_duplicated_template_model_full_name(self):
        """Checks if a second template model is saved having a duplicated first name."""
        TemplateModel(**self._template_model_values).save()

        template_model_two_values = helper.build_template_model_dict_data(1)
        template_model_two_values['full_name'] = self._template_model_values['full_name']

        template_model_two = TemplateModel(**template_model_two_values)

        exceptions = (Sqlite3IntegrityError, DjangoIntegrityError)
        with self.assertRaises(expected_exception=exceptions):
            template_model_two.save()

    def test_save_template_model_null_full_name(self):
        """Checks if a template model is saved having a null full name."""
        template_model_values = helper.build_template_model_dict_data()
        del template_model_values['full_name']

        template_model = TemplateModel(**template_model_values)
        template_model.save()

        self.assertTrue(template_model.id)

    def test_save_template_model_full_name_length(self):
        """Checks if a template model is saved having a full name greater than its max length."""
        template_model_test_values = helper.build_template_model_dict_data()

        max_length = 150
        template_model_test_values['full_name'] = ''.join(['a' for i in range(max_length+1)])
        template_model = TemplateModel(**template_model_test_values)

        exceptions = (Sqlite3IntegrityError, DjangoIntegrityError)
        with self.assertRaises(expected_exception=exceptions):
            template_model.save()

    @freezegun.freeze_time('2020-03-10 00:00:00')
    def test_save_template_model_created_at_auto_now_add(self):
        """Checks if a template model is saved with the correct created at based on auto now add."""
        template_model = TemplateModel(**self._template_model_values)
        template_model.save()

        self.assertEqual(
            datetime.datetime.strftime(template_model.created_at, '%Y-%m-%d %H:%M:%S'),
            '2020-03-10 00:00:00'
        )

    @freezegun.freeze_time('2020-03-10 00:00:00')
    def test_save_template_model_updated_at_auto_now_add(self):
        """Checks if a template model is saved with the correct updated at based on auto now."""
        template_model = TemplateModel(**self._template_model_values)
        template_model.save()

        self.assertEqual(
            datetime.datetime.strftime(template_model.updated_at, '%Y-%m-%d %H:%M:%S'),
            '2020-03-10 00:00:00'
        )
