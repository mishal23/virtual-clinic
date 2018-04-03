import unittest
from django.test import TestCase
from django.urls import resolve
from server.views_medtest import *

class TestMedicalTest(TestCase):

	def test_medtest_upload(self):
		found = resolve('/medtest/upload/')
		self.assertEqual(found.func, create_view )

	def test_medtest_list(self):
		found = resolve('/medtest/list/')
		self.assertEqual(found.func, list_view )
	
	def test_medtest_display(self):
		found = resolve('/medtest/display/')
		self.assertEqual(found.func, display_view )
	
	def test_medtest_update(self):
		found = resolve('/medtest/update/')
		self.assertEqual(found.func, update_view )


