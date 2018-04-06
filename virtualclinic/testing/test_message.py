import unittest
from django.test import TestCase
from django.urls import resolve
from server.views_message import *
import colorama
from colorama import Fore, Style

class TestMessage(TestCase):

	def test_list_messages(self):
		found = resolve('/message/list/')
		print(Fore.YELLOW + "Testing list messages")
		print(Style.RESET_ALL)
		result = self.assertEqual(found.func, list_view)
		if result == None:
			print(Fore.GREEN + "list messages verified")
			print(Style.RESET_ALL)

	def test_new_message(self):
		found = resolve('/message/new/')
		print(Fore.YELLOW + "Testing new messages")
		print(Style.RESET_ALL)
		result = self.assertEqual(found.func, new_view)
		if result == None:
			print(Fore.GREEN + "new messages verified")
			print(Style.RESET_ALL)
