from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.db.models import Q

from server.forms import AppointmentForm
from server.models import Account, Appointment, Action
from server import views
from server import appointment
from server import logger
from server import message


def list_view(request):
    # Authentication check
    authentication_result = views.authentication_check(
        request,
        [Account.ACCOUNT_PATIENT, Account.ACCOUNT_DOCTOR]
    )
    if authentication_result is not None:
        return authentication_result
    # Get template data from session
    template_data = views.parse_session(request)
    # Proceed with rest of the view
    appointment.parse_appointment_cancel(request, template_data)     # parse appointment cancelling
    if request.user.account.role == Account.ACCOUNT_DOCTOR:
        template_data['query'] = Appointment.objects.filter(doctor=request.user.account)
    elif request.user.account == Account.ACCOUNT_PATIENT:
        template_data['query'] = Appointment.objects.filter(patient=request.user.account)
    else:
        template_data['query'] = Appointment.objects.all()
    return render(request, 'virtualclinic/appointment/list.html', template_data)


def calendar_view(request):
    # Authentication check
    authentication_result = views.authentication_check(
        request,
        [Account.ACCOUNT_PATIENT, Account.ACCOUNT_DOCTOR]
    )
    if authentication_result is not None:
        return authentication_result
    # Get template data from session
    template_data = views.parse_session(request)
    # Proceed with rest of the view
    appointment.parse_appointment_cancel(request, template_data)  # parse appointment cancelling
    template_data['events'] = appointment.parse_appointments(request)   # Build list of appointments
    return render(request, 'virtualclinic/appointment/calendar.html', template_data)


def update_view(request):
    # Authentication check
    authentication_result = views.authentication_check(request, None, ['pk'])
    if authentication_result is not None:
        return authentication_result
    # Validation check. Make sure appointment exists for given pk
    pk = request.GET['pk']
    try:
        appointment = Appointment.objects.get(pk=pk)
    except Exception:
        request.session['alert_danger'] = "The requested appointment does not exist."
        return HttpResponseRedirect('/error/denied/')
    # Get template data from session
    template_data = views.parse_session(
        request,
        {
            'form_button': "Update Appointment",
            'form_action': "?pk="+pk,
            'appointment': appointment
        }
    )
    # Proceed with rest of the view
    request.POST._mutable = True
    if request.user.account.role == Account.ACCOUNT_PATIENT:
        request.POST['patient'] = request.user.account.pk
    elif request.user.account.role == Account.ACCOUNT_DOCTOR:
        request.POST['doctor'] = request.user.account.pk
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.assign(appointment)
            if Appointment.objects.filter(
                    ~Q(pk=appointment.pk),
                    Q(status="Active"),
                    Q(doctor=appointment.doctor) | Q(patient=appointment.patient),
                    Q(startTime__range=(appointment.startTime, appointment.endTime)) | Q(endTime__range=(appointment.startTime,appointment.endTime))).count():
                form.mark_error('startTime', 'This time conflicts with another appointment.')
                form.mark_error('endTime', 'This time conflicts with another appointment.')
            else:
                appointment.save()
                logger.log(Action.ACTION_APPOINTMENT, 'Appointment Updated', request.user.account)
                template_data['alert_success'] = "The appointment has been updated!"
                template_data['form'] = form
                if request.user.account.role == Account.ACCOUNT_PATIENT:
                    message.send_appointment_update(request, appointment,appointment.doctor)
                elif request.user.account.role == Account.ACCOUNT_DOCTOR:
                    message.send_appointment_update(request, appointment,appointment.patient)
                else:
                    message.send_appointment_update(request, appointment, appointment.patient)
                    message.send_appointment_update(request, appointment, appointment.doctor)
    else:
        form = AppointmentForm(appointment.get_populated_fields())
    if request.user.account.role == Account.ACCOUNT_PATIENT:
        form.disable_field('patient')
    elif request.user.account.role == Account.ACCOUNT_DOCTOR:
        form.disable_field('doctor')
    template_data['form'] = form
    return render(request, 'virtualclinic/appointment/update.html', template_data)


def create_view(request):
    # Authentication check
    authentication_result = views.authentication_check(
        request,
        [Account.ACCOUNT_PATIENT, Account.ACCOUNT_DOCTOR]
    )
    if authentication_result is not None:
        return authentication_result
    # Get template data from session
    template_data = views.parse_session(request, {'form_button':"Create"})
    # Proceed with rest of the view
    default = {}
    if request.user.account.role == Account.ACCOUNT_PATIENT:
        default['patient'] = request.user.account.pk
        if 'doctor' not in request.POST and request.user.account.profile.primaryCareDoctor is not None:
            default['doctor'] = request.user.account.profile.primaryCareDoctor.pk
    elif request.user.account.role == Account.ACCOUNT_DOCTOR:
        default['doctor'] = request.user.account.pk
    if 'hospital' not in request.POST and request.user.account.profile.prefHospital is not None:
        default['hospital'] = request.user.account.profile.prefHospital.pk
    request.POST._mutable = True
    request.POST.update(default)
    form = AppointmentForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            appointment = form.generate()
            if Appointment.objects.filter(
                    Q(status="Active"),
                    Q(doctor=appointment.doctor) | Q(patient=appointment.patient),
                    Q(startTime__range=(appointment.startTime, appointment.endTime)) | Q(endTime__range=(appointment.startTime,appointment.endTime))).count():
                form.mark_error('startTime', 'this time conflicts with another appointment')
                form.mark_error('endTime', 'this time conflicts with another appointment')
            else:
                appointment.save()
                logger.log(Action.ACTION_APPOINTMENT, 'Appointment created', request.user.account)
                form = AppointmentForm(default)     # clean form when page is re displayed
                form._errors = {}
                request.session['alert_success'] = "Successfully created your appointment!"
                if request.user.account.role == Account.ACCOUNT_DOCTOR:
                    message.send_appointment_create(request,appointment,appointment.patient)
                elif request.user.account.role == Account.ACCOUNT_PATIENT:
                    message.send_appointment_create(request, appointment, appointment.doctor)
                else:
                    message.send_appointment_create(request, appointment, appointment.patient)
                    message.send_appointment_create(request, appointment, appointment.doctor)
                return HttpResponseRedirect('/appointment/list/')
    else:
        form._errors = {}
    if request.user.account.role == Account.ACCOUNT_PATIENT:
        form.disable_field('patient')
    elif request.user.account.role == Account.ACCOUNT_DOCTOR:
        form.disable_field('doctor')
    template_data['form'] = form
    return render(request, 'virtualclinic/appointment/create.html',template_data)