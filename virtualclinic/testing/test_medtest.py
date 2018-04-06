import unittest
from django.test import TestCase
from django.urls import resolve
from server.views_medtest import *
import colorama
from colorama import Fore, Style

class TestMedicalTest(TestCase):

	def test_medtest_upload(self):
		found = resolve('/medtest/upload/')
		print(Fore.YELLOW + "Testing medical test upload")
		print(Style.RESET_ALL)
		result = self.assertEqual(found.func, create_view )
		if result == None:
			print(Fore.GREEN + "medical test upload verified")
			print(Style.RESET_ALL)


	def test_medtest_list(self):
		found = resolve('/medtest/list/')
		print(Fore.YELLOW + "Testing medical test list")
		print(Style.RESET_ALL)
		result = self.assertEqual(found.func, list_view )
		if result == None:
			print(Fore.GREEN + "medical test list verified")
			print(Style.RESET_ALL)


	
	def test_medtest_display(self):
		found = resolve('/medtest/display/')
		print(Fore.YELLOW + "Testing medical test display")
		print(Style.RESET_ALL)
		result = self.assertEqual(found.func, display_view )
		if result == None:
			print(Fore.GREEN + "medical test display verified")
			print(Style.RESET_ALL)
	
	def test_medtest_update(self):
		found = resolve('/medtest/update/')
		print(Fore.YELLOW + "Testing medical test update")
		print(Style.RESET_ALL)
		result = self.assertEqual(found.func, update_view )
		if result == None:
			print(Fore.GREEN + "medical test update verified")
			print(Style.RESET_ALL)


