from django.shortcuts import render
from django.http import HttpResponseRedirect

from server.forms import MedicalInfoForm
from server.models import Action, Account, MedicalInfo
from server import logger
from server import views


def list_view(request):
    # Authentication check
    authentication_result = views.authentication_check(
        request,
        [Account.ACCOUNT_DOCTOR]
    )
    if authentication_result is not None:
        return authentication_result
    # Get the template data from the session
    template_data = views.parse_session(request)
    # Proceed with rest of the view
    template_data['query'] = MedicalInfo.objects.filter(account__role=Account.ACCOUNT_PATIENT)
    return render(request,'virtualclinic/medicalinfo/list.html',template_data)


def update_view(request):
    # Authentication check
    authentication_result = views.authentication_check(
        request,
        [Account.ACCOUNT_PATIENT,Account.ACCOUNT_DOCTOR, Account.ACCOUNT_LAB]
    )
    if authentication_result is not None:
        return authentication_result
    # Validation Check. Make sure an appointment exists for the given pk.
    if 'pk' in request.GET:
        if request.user.account.role != Account.ACCOUNT_DOCTOR:
            request.session['alert_danger'] = "You don't have permission to view the page."
            return HttpResponseRedirect('/error/denied/')
        pk = request.GET['pk']
        try:
            medicalinfo = MedicalInfo.objects.get(pk=pk)
        except Exception:
            request.session['alert_danger'] = "The requested medical info doesn't exist."
            return HttpResponseRedirect('/error/denied/')
    else:
        medicalinfo = MedicalInfo.objects.get(account=request.user.account)
    # Get template data from the session
    template_data = views.parse_session(
        request,{
            'form_button':"Update Medical Info"
        })
    if 'pk' in request.GET:
        template_data['form_action'] = "?pk=" + pk
    # Proceed with rest of the view
    request.POST._mutable = True
    request.POST['account'] = medicalinfo.account.pk
    if request.method == 'POST':
        form = MedicalInfoForm(request.POST)
        if form.is_valid():
            form.assign(medicalinfo)
            medicalinfo.save()
            logger.log(Action.ACTION_MEDICALINFO,'Medical Info Updated', request.user.account)
            template_data['alert_success'] = "The medical info has been updated"
    else:
        form = MedicalInfoForm(medicalinfo.get_populated_fields())
    template_data['form'] = form
    form.disable_field('account')
    return render(request,'virtualclinic/medicalinfo/update.html', template_data)