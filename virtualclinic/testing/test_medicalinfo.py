import unittest
from django.test import TestCase
from django.urls import resolve
from server.views_medicalinfo import *


class TestMedicalInfoViews(TestCase):
	
	def test_medicalinfo_list(self):
		found = resolve('/medicalinfo/list/')
		self.assertEqual(found.func, list_view)

	def test_medicalinfo_update(self):
		found = resolve('/medicalinfo/update/')
		self.assertEqual(found.func, update_view)