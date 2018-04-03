import unittest
from django.test import TestCase
from django.urls import resolve
from server.views_home import *

class TestHomeViews(TestCase):

	def test_login(self):
		found = resolve('/')
		self.assertEqual(found.func, login_view)

	def test_setup(self):
		found = resolve('/setup/')
		self.assertEqual(found.func, setup_view)

	def test_logout(self):
		found = resolve('/logout/')
		self.assertEqual(found.func, logout_view)

	def test_register(self):
		found = resolve('/register/')
		self.assertEqual(found.func, register_view)

	def test_error(self):
		found = resolve('/error/denied/')
		self.assertEqual(found.func, error_denied_view)
