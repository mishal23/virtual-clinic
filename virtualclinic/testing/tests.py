import unittest
from django import forms
from django.test import TestCase
from django.test.client import Client
from django.urls import resolve
from datetime import datetime, date

from server.models import Speciality, Location, Hospital, MedicalInfo, User
from server import views
from server.forms import ProfileForm, validate_birthday, validate_username_exists, validate_username_available

class InvalidUser(TestCase):
	def setUp(self):
		self.client = Client()

	def test_invalidUser(self):
		response = self.client.post('/',{'username':'test@virtualclinic.com','password':'test'})
		self.assertRedirects(response,'/setup/', status_code=302, target_status_code=200, msg_prefix='')


# Testing the forms

