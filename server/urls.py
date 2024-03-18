from django.urls import re_path
from django.conf.urls.static import static
from django.conf import settings

from server import views
from server import views_home
from server import views_profile
from server import views_prescription
from server import views_medtest
from server import views_medicalinfo
from server import views_appointment
from server import views_admin
from server import views_message
from server import views_api
from .views import GeneratePdf

app_name = 'server'

urlpatterns = [
    re_path(r'^$', views_home.login_view, name='index'),
    re_path(r'^logout/$', views_home.logout_view, name='logout'),
    re_path(r'^register/$', views_home.register_view, name='register'),
    re_path(r'^setup/$', views_home.setup_view, name='setup'),

    re_path(r'^error/denied/$', views_home.error_denied_view, name='error/denied'),

    re_path(r'^admin/users/$', views_admin.users_view, name='admin/users'),
    re_path(r'^admin/archive_user', views_admin.user_archive, name='admin/archive_user'),
    re_path(r'^admin/archived_users', views_admin.view_archived_users, name='admin/archived_users'),
    re_path(r'^admin/restore_users', views_admin.restore_user, name='admin/restore_users'),
    re_path(r'^admin/activity/$', views_admin.activity_view, name='admin/activity'),
    re_path(r'^admin/statistics/$', views_admin.statistic_view, name='admin/statistics'),
    re_path(r'^admin/speciality/$', views_admin.view_speciality, name='admin/speciality'),
    re_path(r'^admin/add_speciality/$', views_admin.add_speciality, name='admin/add_speciality'),
    re_path(r'^admin/delete_speciality', views_admin.parse_speciality_delete, name='admin/delete_speciality'),
    re_path(r'^admin/symptom/$', views_admin.view_symptom, name='admin/symptom'),
    re_path(r'^admin/add_symptom/$', views_admin.add_symptom, name='admin/add_symptom'),
    re_path(r'^admin/delete_symptom', views_admin.parse_symptom_delete, name='admin/delete_symptom'),
    re_path(r'^admin/createemployee/$', views_admin.createemployee_view, name='admin/createemployee'),
    re_path(r'^admin/add_hospital/$', views_admin.add_hospital_view, name='admin/add_hospital'),
    re_path(r'^admin/import/$', views_admin.csv_import_view, name='admin/import'),
    re_path(r'^admin/export/$', views_admin.csv_export_view, name='admin/export'),
    re_path(r'^admin/backup/$', views_admin.backup_data, name='admin/backup'),

    re_path(r'^message/list/', views_message.list_view, name='message/list'),
    re_path(r'^message/new/', views_message.new_view, name='message/new'),

    re_path(r'^appointment/list/$', views_appointment.list_view, name='appointment/list'),
    re_path(r'^appointment/calendar/$', views_appointment.calendar_view, name='appointment/calendar'),
    re_path(r'^appointment/update/$', views_appointment.update_view, name='appointment/update'),
    re_path(r'^appointment/create/$', views_appointment.create_view, name='appointment/create'),
    re_path(r'^api/appointments/all/$', views_api.appointment_views, name='api/appointment/all'),

    re_path(r'^profile/$', views_profile.profile_view, name='profile'),
    re_path(r'^profile/update/$', views_profile.update_view, name='profile/update'),
    re_path(r'^profile/password/$', views_profile.password_view, name='profile/password'),

    re_path(r'^medtest/upload/$', views_medtest.create_view, name='medtest/upload'),
    re_path(r'^medtest/list/$', views_medtest.list_view, name='medtest/list'),
    re_path(r'^medtest/display/$', views_medtest.display_view, name='medtest/display'),
    re_path(r'^medtest/update/$', views_medtest.update_view, name='medtest/update'),

    re_path(r'^prescription/create/$', views_prescription.create_view, name='prescription/create'),
    re_path(r'^prescription/list/$', views_prescription.list_view, name='prescription/list'),
    re_path(r'^prescription/update/$', views_prescription.update_view, name='prescription/update'),

    re_path(r'^medicalinfo/list/$', views_medicalinfo.list_view, name='medicalinfo/list'),
    re_path(r'^medicalinfo/update/$', views_medicalinfo.update_view, name='medicalinfo/update'),
    re_path(r'^medicalinfo/patient/$', views_medicalinfo.update_view, name='medicalinfo/patient'),

    re_path(r'^pdf/$', GeneratePdf.as_view()),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
