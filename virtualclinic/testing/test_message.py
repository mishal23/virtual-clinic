import unittest
from django.test import TestCase
from django.urls import resolve
from server.views_message import *

class TestMessage(TestCase):

	def test_list_messages(self):
		found = resolve('/message/list/')
		self.assertEqual(found.func, list_view)

	def test_new_message(self):
		found = resolve('/message/new/')
		self.assertEqual(found.func, new_view)
