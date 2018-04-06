import unittest
from django.test import TestCase
from django.urls import resolve
from server.views_prescription import *
import colorama
from colorama import Fore, Style

class TestPrescriptionViews(TestCase):

	def test_prescription_list(self):
		found = resolve('/prescription/list/')
		print(Fore.YELLOW + "Testing prescription list")
		print(Style.RESET_ALL)
		result = self.assertEqual(found.func, list_view)
		if result == None:
			print(Fore.GREEN + "prescription list verified")
			print(Style.RESET_ALL)


	def test_prescription_new(self):
		found = resolve('/prescription/create/')
		print(Fore.YELLOW + "Testing new prescription")
		print(Style.RESET_ALL)
		result = self.assertEqual(found.func, create_view)
		if result == None:
			print(Fore.GREEN + "new prescription verified")
			print(Style.RESET_ALL)

	def test_prescription_update(self):
		found = resolve('/prescription/update/')
		print(Fore.YELLOW + "Testing update prescription")
		print(Style.RESET_ALL)
		result = self.assertEqual(found.func, update_view)
		if result == None:
			print(Fore.GREEN + "update prescription verified")
			print(Style.RESET_ALL)