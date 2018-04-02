from django.test import TestCase

# Create your tests here.
import unittest
from django.urls import resolve
from server.models import Speciality, Location, Hospital, MedicalInfo
from server import views
from server import views_home
from server.views_home import *
from django.test.client import Client


# Testing Models

class SpecialityTestCase(TestCase):
	""" Test  for Model Speciality """
	def setUp(self):
		Speciality.objects.create(name="ENT",description="Checks for Ear Nose Treatment")

	def testSpeciality(self):
		speciality = Speciality.objects.get(name="ENT")
		self.assertEqual(speciality.description,"Checks for Ear Nose Treatment")



class LocationTestCase(TestCase):
	""" Test for Model Location """

	def setUp(self):
		Location.objects.create(city="Mangalore",zip="575026",state="Karnataka",country="India",address="Mukka")

	def testLocation(self):
		location = Location.objects.get(city="Mangalore")
		self.assertEqual(location.zip,"575026")
		self.assertEqual(location.state,"Karnataka")
		self.assertEqual(location.country,"India")
		self.assertEqual(location.address,"Mukka")


class HospitalTestCase(TestCase):
	""" Test for Model Hospital """
	
	def setUp(self):
		Hospital.objects.create(name="Virtual Clinic",phone="9876543210",location=Location.objects.create(city="Mangalore",zip="575026",state="Karnataka",country="India",address="Mukka"))

	def testHospital(self):
		hospital = Hospital.objects.get(phone="9876543210")
		self.assertEqual(hospital.name,"Virtual Clinic")
		self.assertEqual(hospital.location.city,"Mangalore")
		self.assertEqual(hospital.location.zip,"575026")
		self.assertEqual(hospital.location.state,"Karnataka")
		self.assertEqual(hospital.location.country,"India")
		self.assertEqual(hospital.location.address,"Mukka")


# class ProfileTestCase(TestCase):


# Testing the views

class TestHomeViews(TestCase):

	def test_login(self):
		found = resolve('/')
		self.assertEqual(found.func, login_view)


# class TestMedicalTestViews(TestCase):


# class TestAppointmentViews(TestCase):


# class TestPrescriptionViews(TestCase):


# class TestMedicalInfoViews(TestCase):


# class TestAdminViews(TestCase):


# class TestProfileViews(TestCase):


class InvalidUser(TestCase):
	def setUp(self):
		self.client = Client()

	def test_invalidUser(self):
		response = self.client.post('/',{'username':'test@virtualclinic.com','password':'test'})
		self.assertRedirects(response,'/setup/', status_code=302, target_status_code=200, msg_prefix='')


# Testing the forms
