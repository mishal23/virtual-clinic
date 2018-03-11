from server.models import Message
from server import logger
from server.models import Action

datetime_strftime = "%b %d %Y, %I:%M %p"
datet_strftime = "%b %d, %Y"
rime_strftime = "%I:%M %p"


def parse_message_archive(request, template_data):
    if request.method == 'POST':
        if 'delete' in request.POST and 'pk' in request.POST:
            pk = request.POST['pk']
            try:
                message = Message.objects.get(pk=pk)
            except Exception:
                template_data['alert_danger'] = "Unable to archive the message. Please try again later."
                return
            if message.sender == request.user.account:
                if message.sender_deleted:
                    template_data['alert_danger'] = "That message was already archived."
                    return
                message.sender_deleted = True
            if message.target == request.user.account:
                if message.target_deleted:
                    template_data['alert_danger'] = "That message was already archived."
                    return
                message.target_deleted = True
            message.save()
            logger.log(Action.ACTION_MESSAGE, 'Message Archived', request.user.account)
            template_data['alert_success'] = "The message was archived."


def send_message(sender, target, header, body):
    message = Message(
        target=target,
        sender=sender,
        header=header,
        body=body
    )
    message.save()
    logger.log(Action.ACTION_MESSAGE, 'Message sent', sender)


def send_appointment_update(request, appointment, target):
    send_message(
        request.user.account,
        target,
        "Appointment updated",
        "{0} updated your appointment for '{1}'. It now starts at {2} and ends at {3}.".format(
            request.user.account.__str__(),
            appointment.description,
            appointment.startTime.strftime(datetime_strftime),
            appointment.endTime.strftime(datetime_strftime)
        )
    )


def send_appointment_cancel(request, appointment, target):
    send_message(
        request.user.account,
        target,
        "Appointment cancelled",
        "{0} cancelled your appointment for '{1}'. It now starts at {2} and ends at {3}.".format(
            request.user.account.__str__(),
            appointment.description,
            appointment.startTime.strftime(datetime_strftime),
            appointment.endTime.strftime(datetime_strftime)
        )
    )


def send_appointment_create(request, appointment, target):
    send_message(
        request.user.account,
        target,
        "Appointment created",
        "{0} created an appointment for '{1}'. It starts at {2} and ends at {3}.".format(
            request.user.account.__str__(),
            appointment.description,
            appointment.startTime.strftime(datetime_strftime),
            appointment.endTime.strftime(datetime_strftime)
        )
    )