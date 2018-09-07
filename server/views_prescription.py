from datetime import datetime
from django.shortcuts import render
from django.http import HttpResponseRedirect

from server import logger
from server.forms import PrescriptionForm
from server.models import Account, Prescription, Action
from server import views


def create_view(request):
    # Authentication Check
    authentication_result = views.authentication_check(
        request,
        [Account.ACCOUNT_DOCTOR]
    )
    if authentication_result is not None:
        return authentication_result
    # Get template data from session
    template_data = views.parse_session(request,{'form_button':"Add Prescription"})
    default = {}
    if request.user.account.role == Account.ACCOUNT_DOCTOR:
        default['doctor'] = request.user.account.pk
    if 'date' not in request.POST:
        default['date'] = datetime.now().strftime("%Y-%m-%d")
    request.POST._mutable = True
    request.POST.update(default)
    form = PrescriptionForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            pres = Prescription(
                patient = form.cleaned_data['patient'],
                doctor = form.cleaned_data['doctor'],
                date = form.cleaned_data['date'],
                medication = form.cleaned_data['medication'],
                strength = form.cleaned_data['strength'],
                instruction = form.cleaned_data['instruction'],
                refill = form.cleaned_data['refill'],
            )
            pres.save()
            logger.log(Action.ACTION_PRESCRIPTION,'Prescription Created', request.user.account)
            form = PrescriptionForm(default)   # Clean form data when page is redisplayed
            form._errors = {}
            request.session['alert_success'] = "Successfully added the prescription."
            return HttpResponseRedirect('/prescription/list/')
    else:
        form._errors = {}
    if request.user.account.role == Account.ACCOUNT_DOCTOR:
        form.disable_field('doctor')
        form.date = datetime.today()
    template_data['form'] = form
    return render(request, 'virtualclinic/prescription/create.html', template_data)


def list_view(request):
    # Authentication check
    authentication_result = views.authentication_check(
        request,
        [Account.ACCOUNT_DOCTOR,Account.ACCOUNT_PATIENT,Account.ACCOUNT_CHEMIST]
    )
    if authentication_result is not None:
        return authentication_result
    # get template data from session
    template_data = views.parse_session(request)
    # proceed with rest of the view
    if request.method == 'POST':
        if 'delete' in request.POST and 'pk' in request.POST:
            pk = request.POST['pk']
            try:
                prescription = Prescription.objects.get(pk=pk)
                prescription.active = False
                prescription.save()
                logger.log(Action.ACTION_PRESCRIPTION,'Prescription Cancelled', request.user.account)
                template_data['alert_success'] = "The prescription has been deleted."
            except Exception:
                template_data['alert_danger'] = "Unable to delete the prescription. Please try again later."
    if request.user.account.role == Account.ACCOUNT_DOCTOR:
        prescriptions = Prescription.objects.filter(doctor=request.user.account)
    elif request.user.account.role == Account.ACCOUNT_PATIENT:
        prescriptions = Prescription.objects.filter(patient=request.user.account)
    else:
        prescriptions = Prescription.objects.all()
    template_data['query'] = prescriptions.order_by('date')
    return render(request,'virtualclinic/prescription/list.html',template_data)


def update_view(request):
    # Authentication check
    authentication_result = views.authentication_check(request, None, ['pk'])
    if authentication_result is not None:
        return authentication_result
    # Validation check. Make sure a prescription exists for given pk.
    pk = request.GET['pk']
    try:
        prescription = Prescription.objects.get(pk=pk)
    except Exception:
        request.session['alert_danger'] = "The requested prescription does not exist"
        return HttpResponseRedirect('/error/denied')
    # Get the template data from the session
    template_data = views.parse_session(
        request,
        {
            'form_button': "Update Prescription",
            'form_action': "?pk="+pk,
            'prescription': prescription
        })
    # Proceed with rest of view
    request.POST._mutable = True
    if request.method == 'POST':
        form = PrescriptionForm(request.POST)
        if form.is_valid():
            form.assign(prescription)
            prescription.save()
            logger.log(Action.ACTION_PRESCRIPTION, 'Prescription Updated', request.user.account)
            template_data['alert_success'] = "Prescription has been updated"
            template_data['form'] = form
    else:
        form = PrescriptionForm(prescription.get_populated_fields())
    template_data['form'] = form
    return render(request, 'virtualclinic/prescription/update.html', template_data)