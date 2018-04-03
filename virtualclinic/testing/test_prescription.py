import unittest
from django.test import TestCase
from django.urls import resolve
from server.views_prescription import *

class TestPrescriptionViews(TestCase):

	def test_prescription_list(self):
		found = resolve('/prescription/list/')
		self.assertEqual(found.func, list_view)

	def test_prescription_new(self):
		found = resolve('/prescription/create/')
		self.assertEqual(found.func, create_view)

	def test_prescription_update(self):
		found = resolve('/prescription/update/')
		self.assertEqual(found.func, update_view)