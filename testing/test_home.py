import unittest
from django.test import TestCase
from django.urls import resolve
from server.views_home import *
import colorama
from colorama import Fore, Style

class TestHomeViews(TestCase):

	def test_login(self):
		found = resolve('/')
		print(Fore.YELLOW + "Testing login")
		print(Style.RESET_ALL)
		result = self.assertEqual(found.func, login_view)
		if result == None:
			print(Fore.GREEN + "login verified")
			print(Style.RESET_ALL)

	def test_setup(self):
		found = resolve('/setup/')
		print(Fore.YELLOW + "Testing setup")
		print(Style.RESET_ALL)
		result = self.assertEqual(found.func, setup_view)
		if result == None:
			print(Fore.GREEN + "setup verified")
			print(Style.RESET_ALL)

	def test_logout(self):
		found = resolve('/logout/')
		print(Fore.YELLOW + "Testing logout")
		print(Style.RESET_ALL)
		result = self.assertEqual(found.func, logout_view)
		if result == None:
			print(Fore.GREEN + "logout verified")
			print(Style.RESET_ALL)


	def test_register(self):
		found = resolve('/register/')
		print(Fore.YELLOW + "Testing register")
		print(Style.RESET_ALL)
		result = self.assertEqual(found.func, register_view)
		if result == None:
			print(Fore.GREEN + "register verified")
			print(Style.RESET_ALL)


	def test_error(self):
		found = resolve('/error/denied/')
		print(Fore.YELLOW + "Testing register error")
		print(Style.RESET_ALL)
		result = self.assertEqual(found.func, error_denied_view)
		if result == None:
			print(Fore.GREEN + "register error verified")
			print(Style.RESET_ALL)
