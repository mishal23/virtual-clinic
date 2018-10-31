from datetime import datetime
from django.shortcuts import render
from django.http import HttpResponseRedirect

from server.forms import MedTestForm, MedTestDisplayForm
from server.models import Account, Action, MedicalTest
from server import logger
from server import views


def create_view(request):
    # Authentication check
    authentication_result = views.authentication_check(
        request,
        [Account.ACCOUNT_DOCTOR, Account.ACCOUNT_LAB]
    )
    if authentication_result is not None:
        return authentication_result
    # get template data from session
    template_data = views.parse_session(request, {'form_button': "Upload"})
    # proceed with rest of the view
    default = {}
    if request.user.account.role == Account.ACCOUNT_DOCTOR:
        default['doctor'] = request.user.account.pk
    if 'hospital' not in request.POST and request.user.account.profile.prefHospital is not None:
        default['hospital'] = request.user.account.profile.prefHospital.pk
    if 'date' not in request.POST:
        default['date'] = datetime.now().strftime("%Y-%m-%d")
    request.POST._mutable = True
    request.POST.update(default)
    form = MedTestForm(request.POST,request.FILES)
    if request.method == 'POST':
        if form.is_valid():
            medicaltest = form.generate()
            medicaltest.save()
            logger.log(Action.ACTION_MEDTEST,'Medical Test Created', request.user.account)
            form = MedTestForm(default)  # clean form data
            #form.disable_field('doctor')
            form._errors = {}
            template_data['alert_success'] = "Successfully uploaded medical test"
    else:
        form._errors = {}
    #form.disable_field('doctor')
    template_data['form'] = form
    return render(request,'virtualclinic/medtest/upload.html', template_data)


def list_view(request):
    # Authentication check
    authentication_result = views.authentication_check(
        request,
        [Account.ACCOUNT_DOCTOR, Account.ACCOUNT_PATIENT, Account.ACCOUNT_LAB]
    )
    if authentication_result is not None:
        return authentication_result
    # get template data from session
    template_data = views.parse_session(request)
    # proceed with rest of the view
    if request.user.account.role == Account.ACCOUNT_DOCTOR:
        template_data['query'] = MedicalTest.objects.all()
    elif request.user.account.role == Account.ACCOUNT_LAB:
        template_data['query'] = MedicalTest.objects.all()
    else:
        template_data['query'] = MedicalTest.objects.filter(private=False)
    return render(request, 'virtualclinic/medtest/list.html', template_data)


def display_view(request):
    # Authentication check
    authentication_result = views.authentication_check(
        request,
        None,
        ['pk']
    )
    if authentication_result is not None:
        return authentication_result
    # Validation check. Make sure a medical test exists for given pk
    pk = request.GET['pk']
    try:
        medicaltest = MedicalTest.objects.get(pk=pk)
    except Exception:
        request.session['alert_danger'] = "The requested medical test does not exist"
        return HttpResponseRedirect('/error/denied/')
    # get template data from the session
    template_data = views.parse_session(
        request,
        {
            'form_button': "Return to list of Medical Tests",
            'form_action': "?pk="+pk,
            'medtest' : medicaltest
        })
    # Proceed with the rest of view
    if request.method == 'GET':
        form = MedTestDisplayForm(medicaltest.get_populated_fields())
        form.disable_field('name')
        form.disable_field('date')
        form.disable_field('hospital')
        form.disable_field('description')
        form.disable_field('doctor')
        form.disable_field('patient')
        form.disable_field('private')
        form.disable_field('completed')

        template_data['form'] = form

        template_data['img'] = medicaltest.image1
        template_data['img2'] = medicaltest.image2
        template_data['img3'] = medicaltest.image3
        template_data['img4'] = medicaltest.image4
        template_data['img5'] = medicaltest.image5
    else:
        return HttpResponseRedirect('/medtest/list')
    return render(request, 'virtualclinic/medtest/display.html', template_data)


def update_view(request):
    # Authentication check
    authentication_result = views.authentication_check(request, None, ['pk'])
    if authentication_result is not None:
        return authentication_result
    # Validation check. Make sure a medical test exists for given pk.
    pk = request.GET['pk']
    try:
        medicaltest = MedicalTest.objects.get(pk=pk)
    except Exception:
        request.session['alert_danger'] = "The requested medical test does not exist"
        return HttpResponseRedirect('/error/denied')
    # Get the template data from the session
    template_data = views.parse_session(
        request,
        {
            'form_button':"Update Medical Test",
            'form_action':"?pk="+pk,
            'medtest':medicaltest
        })
    # Proceed with rest of view
    request.POST._mutable = True
    if  request.user.account.role == Account.ACCOUNT_DOCTOR:
        request.POST['doctor'] = request.user.account.pk
    if request.method == 'POST':
        form = MedTestForm(request.POST)
        if form.is_valid():
            form.assign(medicaltest)
            medicaltest.save()
            logger.log(Action.ACTION_MEDTEST, 'Medical test Updated', request.user.account)
            template_data['alert_success'] = "Medical test has been updated"
            template_data['form'] = form
    else:
        form = MedTestForm(medicaltest.get_populated_fields())
    if request.user.account.role == Account.ACCOUNT_DOCTOR:
        form.disable_field('doctor')
    template_data['form'] = form
    return render(request,'virtualclinic/medtest/update.html', template_data)
