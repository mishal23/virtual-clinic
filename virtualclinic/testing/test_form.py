import unittest
from django import forms
from django.test import TestCase
from datetime import datetime, date

from server.models import Location, Hospital
from server.forms import ProfileForm

class TestProfileForm(TestCase):

	def setUp(self):
		birthday = datetime.now()
		location_data = Location.objects.create(
				city="Mangalore",
				zip="575025",
				state="Karnataka",
				country="India",
				address="None"
			)
		test_hospital = Hospital.objects.create(location=location_data)

		self.form_data = {
			'firstname':"Test",
			'lastname' :"Test",
			'sex':'M',
			'birthday': birthday,
			'phone':"9989727245",
			'allergies':"Sand",
			'created':datetime.now(),
			'prefHospital':test_hospital.id,
		}

	def test_valid_profile_form(self):
		form = ProfileForm(data=self.form_data)
		self.assertTrue(form.is_valid())
