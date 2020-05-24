from django.conf.urls import url
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
    url(r'^$', views_home.login_view, name='index'),
    url(r'^logout/$', views_home.logout_view, name='logout'),
    url(r'^register/$', views_home.register_view, name='register'),
    url(r'^setup/$', views_home.setup_view, name='setup'),

    url(r'^error/denied/$', views_home.error_denied_view, name='error/denied'),

    url(r'^admin/users/$', views_admin.users_view, name='admin/users'),
    url(r'^admin/archive_user', views_admin.user_archive, name='admin/archive_user'),
    url(r'^admin/archived_users', views_admin.view_archived_users, name='admin/archived_users'),
    url(r'^admin/restore_users', views_admin.restore_user, name='admin/restore_users'),
    url(r'^admin/activity/$', views_admin.activity_view, name='admin/activity'),
    url(r'^admin/statistics/$', views_admin.statistic_view, name='admin/statistics'),
    url(r'^admin/speciality/$', views_admin.view_speciality, name='admin/speciality'),
    url(r'^admin/add_speciality/$', views_admin.add_speciality, name='admin/add_speciality'),
    url(r'^admin/delete_speciality', views_admin.parse_speciality_delete, name='admin/delete_speciality'),
    url(r'^admin/symptom/$', views_admin.view_symptom, name='admin/symptom'),
    url(r'^admin/add_symptom/$', views_admin.add_symptom, name='admin/add_symptom'),
    url(r'^admin/delete_symptom', views_admin.parse_symptom_delete, name='admin/delete_symptom'),
    url(r'^admin/createemployee/$', views_admin.createemployee_view, name='admin/createemployee'),
    url(r'^admin/add_hospital/$', views_admin.add_hospital_view, name='admin/add_hospital'),
    url(r'^admin/import/$', views_admin.csv_import_view, name='admin/import'),
    url(r'^admin/export/$', views_admin.csv_export_view, name='admin/export'),
    url(r'^admin/backup/$', views_admin.backup_data, name='admin/backup'),

    url(r'^message/list/', views_message.list_view, name='message/list'),
    url(r'^message/new/', views_message.new_view, name='message/new'),

    url(r'^appointment/list/$', views_appointment.list_view, name='appointment/list'),
    url(r'^appointment/calendar/$', views_appointment.calendar_view, name='appointment/calendar'),
    url(r'^appointment/update/$', views_appointment.update_view, name='appointment/update'),
    url(r'^appointment/create/$', views_appointment.create_view, name='appointment/create'),
    url(r'^api/appointments/all/$', views_api.appointment_views, name='api/appointment/all'),

    url(r'^profile/$', views_profile.profile_view, name='profile'),
    url(r'^profile/update/$', views_profile.update_view, name='profile/update'),
    url(r'^profile/password/$', views_profile.password_view, name='profile/password'),

    url(r'^medtest/upload/$', views_medtest.create_view, name='medtest/upload'),
    url(r'^medtest/list/$', views_medtest.list_view, name='medtest/list'),
    url(r'^medtest/display/$', views_medtest.display_view, name='medtest/display'),
    url(r'^medtest/update/$', views_medtest.update_view, name='medtest/update'),

    url(r'^prescription/create/$', views_prescription.create_view, name='prescription/create'),
    url(r'^prescription/list/$', views_prescription.list_view, name='prescription/list'),
    url(r'^prescription/update/$', views_prescription.update_view, name='prescription/update'),

    url(r'^medicalinfo/list/$', views_medicalinfo.list_view, name='medicalinfo/list'),
    url(r'^medicalinfo/update/$', views_medicalinfo.update_view, name='medicalinfo/update'),
    url(r'^medicalinfo/patient/$', views_medicalinfo.update_view, name='medicalinfo/patient'),

    url(r'^pdf/$', GeneratePdf.as_view()),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
