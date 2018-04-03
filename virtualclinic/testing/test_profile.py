import unittest
from django.test import TestCase
from django.urls import resolve
from server.views_profile import *

class TestProfileViews(TestCase):

	def test_profile(self):
		found = resolve('/profile/')
		self.assertEqual(found.func, profile_view)

	def test_profile_update(self):
		found = resolve('/profile/update/')
		self.assertEqual(found.func, update_view)

	def test_password(self):
		found = resolve('/profile/password/')
		self.assertEqual(found.func, password_view)