import unittest
from django.test import TestCase
from django.urls import resolve

from server.views_admin import *

# Test for Admin Views

class TestAdminViews(TestCase):

	def test_specilaity_delete(self):
		found = resolve('/admin/delete_speciality/')
		self.assertEqual(found.func, parse_speciality_delete)

	def test_symptom_delete(self):
		found = resolve('/admin/delete_symptom/')
		self.assertEqual(found.func, parse_symptom_delete)

	def test_user_archive(self):
		found = resolve('/admin/archive_user/')
		self.assertEqual(found.func, user_archive)

	def test_view_archived_users(self):
		found = resolve('/admin/archived_users/')
		self.assertEqual(found.func, view_archived_users)

	def test_restore_user(self):
		found = resolve('/admin/restore_users/')
		self.assertEqual(found.func, restore_user)

	def test_users(self):
		found = resolve('/admin/users/')
		self.assertEqual(found.func, users_view)

	def test_activity_view(self):
		found = resolve('/admin/activity/')
		self.assertEqual(found.func, activity_view)

	def test_speciality_view(self):
		found = resolve('/admin/speciality/')
		self.assertEqual(found.func, view_speciality)

	def test_symptom_view(self):
		found = resolve('/admin/symptom/')
		self.assertEqual(found.func, view_symptom)	

	def test_add_speciality(self):
		found = resolve('/admin/add_speciality/')
		self.assertEqual(found.func, add_speciality)

	def test_add_symptom(self):
		found = resolve('/admin/add_symptom/')
		self.assertEqual(found.func, add_symptom)

	def test_add_hopsital(self):
		found = resolve('/admin/add_hospital/')
		self.assertEqual(found.func, add_hospital_view)

	def test_create_employee(self):
		found = resolve('/admin/createemployee/')
		self.assertEqual(found.func, createemployee_view)

	def test_statistic_view(self):
		found = resolve('/admin/statistics/')
		self.assertEqual(found.func, statistic_view)

	def test_import(self):
		found = resolve('/admin/import/')
		self.assertEqual(found.func, csv_import_view)

	def test_export(self):
		found = resolve('/admin/export/')
		self.assertEqual(found.func, csv_export_view)	
