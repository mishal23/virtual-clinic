import unittest
from django import forms
from django.test import TestCase
from datetime import datetime, date

from server.models import User
from server.forms import validate_birthday, validate_username_exists, validate_username_available
import colorama
from colorama import Fore, Style

class TestFormValidators(TestCase):
	def setUp(self):
		self.birthday = date(1000,1,1)

	def test_validate_lower_bound_birthday(self):
		self.assertRaises(forms.ValidationError, validate_birthday, self.birthday)

	def test_validate_upper_bound_birthday(self):
		self.birthday = date(2030,12,12)
		self.assertRaises(forms.ValidationError, validate_birthday, self.birthday)

	def test_validate_birthday(self):
		self.birthday = date(1998,8,23)
		self.assertIsNone(validate_birthday(self.birthday))

	def test_validate_username_exists(self):
		User.objects.create(username="test@virtualclinic.com",password="test")
		self.assertRaises(forms.ValidationError,validate_username_exists,'test1@virtualclinic.com' )

	def test_validate_username_available(self):
		User.objects.create(username="test@virtualclinic.com",password="test")
		self.assertRaises(forms.ValidationError, validate_username_available, "test@virtualclinic.com")
