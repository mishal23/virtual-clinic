import unittest
from django.test import TestCase
from django.urls import resolve
from server.views_appointment import *
import colorama
from colorama import Fore, Style

class TestAppointmentViews(TestCase):

	def test_appointment_list(self):
		from server.views_appointment import list_view
		print(Fore.YELLOW + "Testing appointment list")
		print(Style.RESET_ALL)
		found = resolve('/appointment/list/')
		result=self.assertEqual(found.func, list_view)
		if result == None:
			print(Fore.GREEN + "appointment list verified")
			print(Style.RESET_ALL)

	def test_appointment_calendar(self):
		from server.views_appointment import calendar_view
		print(Fore.YELLOW + "Testing appointment calender")
		print(Style.RESET_ALL)
		found = resolve('/appointment/calendar/')
		result=self.assertEqual(found.func, calendar_view)
		if result == None:
			print(Fore.GREEN + "appointment calender verified")
			print(Style.RESET_ALL)

	def test_appointment_update(self):
		from server.views_appointment import update_view
		print(Fore.YELLOW + "Testing appointment update")
		print(Style.RESET_ALL)
		found = resolve('/appointment/update/')
		result=self.assertEqual(found.func, update_view)
		if result == None:
			print(Fore.GREEN + "appointment update verified")
			print(Style.RESET_ALL)

	def test_appointment_create(self):
		from server.views_appointment import create_view
		print(Fore.YELLOW + "Testing appointment create")
		print(Style.RESET_ALL)
		found = resolve('/appointment/create/')
		result=self.assertEqual(found.func, create_view)
		if result == None:
			print(Fore.GREEN + "appointment create verified")
			print(Style.RESET_ALL)
