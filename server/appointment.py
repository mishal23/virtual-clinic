from django.utils.safestring import mark_safe
from django.utils import timezone

from server.models import Account, Appointment, Action
from server import logger
from server import message
from server.views import sanitize_js
from server.message import datetime_strftime


def parse_appointments(request):
    if request.user.account.role == Account.ACCOUNT_PATIENT:
        appointments = Appointment.objects.filter(status="Active", patient=request.user.account)
    elif request.user.account.role == Account.ACCOUNT_DOCTOR:
        appointments = Appointment.objects.filter(status="Active", doctor=request.user.account)
    else:
        appointments = Appointment.objects.filter(status="Active")
    body = []
    if appointments.count() > 0:
        for appointment in appointments:
            body.append("{")
            body.append("id: {0},".format(appointment.pk))
            body.append(
                "formatted_start: '{0}',".format(timezone.localtime(appointment.startTime).strftime(datetime_strftime)))
            body.append(
                "formatted_end: '{0}',".format(timezone.localtime(appointment.endTime).strftime(datetime_strftime)))
            body.append("hospital: '{0}',".format(sanitize_js(appointment.hospital.name)))
            body.append("patient: '{0}',".format(sanitize_js(appointment.doctor.__str__())))
            body.append("doctor: '{0}',".format(sanitize_js(appointment.patient.__str__())))
            if request.user.account.role == Account.ACCOUNT_PATIENT:
                message = "{0}, {1}".format(appointment.doctor.profile, appointment.description)
            else:
                message = "{0}, {1}".format(appointment.patient.profile, appointment.description)
            body.append("title: '{0}',".format(sanitize_js(message)))
            stime = timezone.localtime(appointment.startTime)
            sdate = stime.date()
            stime = stime.time()
            body.append(
                "start: new Date({0},{1},{2},{3},{4}),".format(sdate.year, sdate.month - 1, sdate.day, stime.hour,
                                                               stime.minute))
            stime = timezone.localtime(appointment.endTime)
            sdate = stime.date()
            stime = stime.time()
            body.append("end: new Date({0},{1},{2},{3},{4})".format(sdate.year, sdate.month - 1, sdate.day, stime.hour,
                                                                    stime.minute))
            body.append("},")
        return mark_safe('\n'.join(body)[:-1])
    return mark_safe("")


def parse_appointment_cancel(request, template_data):
    if request.method == 'POST':
        if 'cancel' in request.POST and 'pk' in request.POST:
            pk = request.POST['pk']
            try:
                appointment = Appointment.objects.get(pk=pk)
            except Exception:
                template_data['alert_danger'] = "Unable to cancel the appointment. Please try again later."
                return
            if request.user.account.role == Account.ACCOUNT_PATIENT and request.user.account != appointment.patient:
                template_data['alert_danger'] = "You don't have permission to cancel that appointment."
                return
            elif request.user.account.role == Account.ACCOUNT_DOCTOR and request.user.account != appointment.doctor:
                template_data['alert_danger'] = "You don't have permission to cancel that appointment."
                return
            elif appointment.status == "Cancelled":
                template_data['alert_danger'] = "That appointment was already cancelled."
                return
            appointment.status = "Cancelled"
            appointment.save()
            logger.log(Action.ACTION_APPOINTMENT, 'Appointment cancelled', request.user.account)
            if request.user.account.role == Account.ACCOUNT_DOCTOR:
                message.send_appointment_cancel(request, appointment, appointment.patient)
            if request.user.account.role == Account.ACCOUNT_PATIENT:
                message.send_appointment_cancel(request, appointment, appointment.doctor)
            template_data['alert_success'] = "The appointment has been cancelled."

