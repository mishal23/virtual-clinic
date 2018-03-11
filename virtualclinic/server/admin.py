from django.contrib import admin
from server.models import Location, Hospital , Account, Profile, Action, Appointment, MedicalTest


class LocationAdmin(admin.ModelAdmin):
    fields = ['city', 'zip', 'state', 'country', 'address']
    list_display = ('address', 'city', 'state', 'country', 'zip')


admin.site.register(Location,LocationAdmin)


class HospitalAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Name', {'fields': ['name']}),
        ('Phone', {'fields': ['phone']}),
        ('Location', {'fields': ['location']}),
    ]
    list_display = ('name', 'location', 'phone')


admin.site.register(Hospital,HospitalAdmin)


class AccountAdmin(admin.ModelAdmin):
    fields = ['role', 'profile', 'user']
    list_display = ('role', 'profile')


admin.site.register(Account, AccountAdmin)


class ProfileAdmin(admin.ModelAdmin):
    fields = [
        'firstname',
        'lastname',
        'sex',
        'birthday',
        'phone',
        'allergies'
    ]
    list_display = ('firstname', 'lastname', 'birthday', 'created')


admin.site.register(Profile, ProfileAdmin)


class ActionAdmin(admin.ModelAdmin):
    readonly_fields = ('timePerformed',)
    fields = [
        'type',
        'description',
        'account',
    ]
    list_display = ('account', 'type', 'description', 'timePerformed')
    list_filter = ('account', 'type', 'timePerformed')
    ordering = ('-timePerformed',)


admin.site.register(Action, ActionAdmin)


class AppointmentAdmin(admin.ModelAdmin):
    fields = [
        'doctor',
        'patient',
        'description',
        'status',
        'hospital',
        'startTime',
        'endTime'
    ]
    list_display = ('description', 'hospital', 'doctor', 'patient', 'startTime', 'endTime', 'status')


admin.site.register(Appointment, AppointmentAdmin)


class MedicalTestAdmin(admin.ModelAdmin):
    fields = [
        'name',
        'date',
        'hospital',
        'description',
        'doctor',
        'patient',
        'private',
        'completed',
        'image1'
    ]
    list_display = ('name', 'doctor', 'patient', 'date')


admin.site.register(MedicalTest, MedicalTestAdmin)