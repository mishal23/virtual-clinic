import unittest
from django.test import TestCase
from django.urls import resolve
from server.views_appointment import *

class TestAppointmentViews(TestCase):

	def test_appointment_list(self):
		from server.views_appointment import list_view
		found = resolve('/appointment/list/')
		self.assertEqual(found.func, list_view)

	def test_appointment_calendar(self):
		from server.views_appointment import calendar_view
		found = resolve('/appointment/calendar/')
		self.assertEqual(found.func, calendar_view)

	def test_appointment_update(self):
		from server.views_appointment import update_view
		found = resolve('/appointment/update/')
		self.assertEqual(found.func, update_view)

	def test_appointment_create(self):
		from server.views_appointment import create_view
		found = resolve('/appointment/create/')
		self.assertEqual(found.func, create_view)
