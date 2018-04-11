import unittest
from django.test import TestCase
from django.urls import resolve

from server.views_admin import *
import colorama
from colorama import Fore, Style

# Test for Admin Views

class TestAdminViews(TestCase):

	def test_specilaity_delete(self):
		print(Fore.YELLOW + "Testing Speciality delete")
		print(Style.RESET_ALL)
		found = resolve('/admin/delete_speciality/')
		result = self.assertEqual(found.func, parse_speciality_delete)
		if result == None:
			print(Fore.GREEN + "Speciality delete verified")
			print(Style.RESET_ALL)

	def test_symptom_delete(self):
		print(Fore.YELLOW + "Testing Symptom delete")
		print(Style.RESET_ALL)
		found = resolve('/admin/delete_symptom/')
		result = self.assertEqual(found.func, parse_symptom_delete)
		if result == None:
			print(Fore.GREEN + "Symptom delete verified")
			print(Style.RESET_ALL)

	def test_user_archive(self):
		print(Fore.YELLOW + "Testing User archive")
		print(Style.RESET_ALL)
		found = resolve('/admin/archive_user/')
		result = self.assertEqual(found.func, user_archive)
		if result == None:
			print(Fore.GREEN + "User archive verified")
			print(Style.RESET_ALL)


	def test_view_archived_users(self):
		print(Fore.YELLOW + "Testing view archive users")
		print(Style.RESET_ALL)
		found = resolve('/admin/archived_users/')
		result = self.assertEqual(found.func, view_archived_users)
		if result == None:
			print(Fore.GREEN + "View archive verified")
			print(Style.RESET_ALL)

	def test_restore_user(self):
		print(Fore.YELLOW + "Testing restore users")
		print(Style.RESET_ALL)

		found = resolve('/admin/restore_users/')
		result=self.assertEqual(found.func, restore_user)
		if result == None:
			print(Fore.GREEN + "Restore user verified")
			print(Style.RESET_ALL)

	def test_users(self):
		print(Fore.YELLOW + "Testing users")
		print(Style.RESET_ALL)
		found = resolve('/admin/users/')
		result=self.assertEqual(found.func, users_view)
		if result == None:
			print(Fore.GREEN + "user verified")
			print(Style.RESET_ALL)

	def test_activity_view(self):
		print(Fore.YELLOW + "Testing activity view")
		print(Style.RESET_ALL)
		found = resolve('/admin/activity/')
		result=self.assertEqual(found.func, activity_view)
		if result == None:
			print(Fore.GREEN + "activity view verified")
			print(Style.RESET_ALL)

	def test_speciality_view(self):
		print(Fore.YELLOW + "Testing speciality view")
		print(Style.RESET_ALL)
	
		found = resolve('/admin/speciality/')
		result=self.assertEqual(found.func, view_speciality)
		if result == None:
			print(Fore.GREEN + "speciality view verified")
			print(Style.RESET_ALL)

	def test_symptom_view(self):
		print(Fore.YELLOW + "Testing symptom view")
		print(Style.RESET_ALL)
	
		found = resolve('/admin/symptom/')
		result=self.assertEqual(found.func, view_symptom)
		if result == None:
			print(Fore.GREEN + "symptom view verified")
			print(Style.RESET_ALL)	

	def test_add_speciality(self):
		print(Fore.YELLOW + "Testing add speciality")
		print(Style.RESET_ALL)
	
		found = resolve('/admin/add_speciality/')
		result=self.assertEqual(found.func, add_speciality)
		if result == None:
			print(Fore.GREEN + "add speciality verified")
			print(Style.RESET_ALL)

	def test_add_symptom(self):
		print(Fore.YELLOW + "Testing add symptom")
		print(Style.RESET_ALL)
	
		found = resolve('/admin/add_symptom/')
		result=self.assertEqual(found.func, add_symptom)
		if result == None:
			print(Fore.GREEN + "add symptom verified")
			print(Style.RESET_ALL)

	def test_add_hopsital(self):
		print(Fore.YELLOW + "Testing add hospital")
		print(Style.RESET_ALL)
	
		found = resolve('/admin/add_hospital/')
		result=self.assertEqual(found.func, add_hospital_view)
		if result == None:
			print(Fore.GREEN + "add hospital verified")
			print(Style.RESET_ALL)

	def test_create_employee(self):
		print(Fore.YELLOW + "Testing create employee")
		print(Style.RESET_ALL)
		found = resolve('/admin/createemployee/')
		result=self.assertEqual(found.func, createemployee_view)
		if result == None:
			print(Fore.GREEN + "create employee verified")
			print(Style.RESET_ALL)
			
	def test_statistic_view(self):
		print(Fore.YELLOW + "Testing statistic view")
		print(Style.RESET_ALL)
		found = resolve('/admin/statistics/')
		result = self.assertEqual(found.func, statistic_view)
		if result == None:
			print(Fore.GREEN + "statistic view verified")
			print(Style.RESET_ALL)

	def test_import(self):
		print(Fore.YELLOW + "Testing import")
		print(Style.RESET_ALL)
		found = resolve('/admin/import/')
		result=self.assertEqual(found.func, csv_import_view)
		if result == None:
			print(Fore.GREEN + "statistic view verified")
			print(Style.RESET_ALL)

	def test_export(self):
		print(Fore.YELLOW + "Testing export")
		print(Style.RESET_ALL)
		found = resolve('/admin/export/')
		result=self.assertEqual(found.func, csv_export_view)
		if result == None:
			print(Fore.GREEN + "test export verified")
			print(Style.RESET_ALL)

	def test_backup(self):
		print(Fore.YELLOW + "Testing backup")
		print(Style.RESET_ALL)
		found = resolve('/admin/backup/')
		result=self.assertEqual(found.func, backup_data)
		if result == None:
			print(Fore.GREEN + "test backup verified")
			print(Style.RESET_ALL)		
