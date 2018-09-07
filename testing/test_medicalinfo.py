import unittest
from django.test import TestCase
from django.urls import resolve
from server.views_medicalinfo import *
import colorama
from colorama import Fore, Style

class TestMedicalInfoViews(TestCase):
	
	def test_medicalinfo_list(self):
		found = resolve('/medicalinfo/list/')
		print(Fore.YELLOW + "Testing medical info list")
		print(Style.RESET_ALL)
		result = self.assertEqual(found.func, list_view)
		if result == None:
			print(Fore.GREEN + "medical info list verified")
			print(Style.RESET_ALL)


	def test_medicalinfo_update(self):
		found = resolve('/medicalinfo/update/')
		print(Fore.YELLOW + "Testing medical info update")
		print(Style.RESET_ALL)
		result = self.assertEqual(found.func, update_view)
		if result == None:
			print(Fore.GREEN + "medical info update verified")
			print(Style.RESET_ALL)