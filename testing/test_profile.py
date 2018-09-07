import unittest
from django.test import TestCase
from django.urls import resolve
from server.views_profile import *
import colorama
from colorama import Fore, Style

class TestProfileViews(TestCase):

	def test_profile(self):
		found = resolve('/profile/')
		print(Fore.YELLOW + "Testing profile")
		print(Style.RESET_ALL)
		result = self.assertEqual(found.func, profile_view)
		if result == None:
			print(Fore.GREEN + "profile verified")
			print(Style.RESET_ALL)


	def test_profile_update(self):
		found = resolve('/profile/update/')
		print(Fore.YELLOW + "Testing profile update")
		print(Style.RESET_ALL)
		result = self.assertEqual(found.func, update_view)
		if result == None:
			print(Fore.GREEN + "profile update verified")
			print(Style.RESET_ALL)

	def test_password(self):
		found = resolve('/profile/password/')
		print(Fore.YELLOW + "Testing setup password")
		print(Style.RESET_ALL)
		result = self.assertEqual(found.func, password_view)
		if result == None:
			print(Fore.GREEN + "setup password verified")
			print(Style.RESET_ALL)