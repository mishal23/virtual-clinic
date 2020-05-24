from rest_framework.decorators import api_view
from rest_framework.response import Response
from server.models import Appointment
import json


@api_view(['GET'])
def appointment_views(request):
	"""
	HEAVY NOTE: Never write API like this, this is just to test!
	"""
	res = Appointment.objects.all()
	response = []
	for r in res:
		temp_res = {}
		temp_res['patient'] = r.patient.profile.firstname + " " + r.patient.profile.lastname
		temp_res['description'] = r.description
		temp_res['start_time'] = r.startTime
		temp_res['end_time'] = r.endTime
		response.append(temp_res)
		
	return Response(list(response))