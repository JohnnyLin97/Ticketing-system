from .models import Event1_seats
from django.http import HttpResponse
import json
import random
from .db_helper import retrieve_all_seats

# Create your views here.
def retrieve(request):
    try:
        all_seats = retrieve_all_seats()
    
    except Exception as e: 
        print(e)

    response_data = {}
    response_data['result'] = 'error'
    response_data['message'] = 'Some error message'

    return HttpResponse(json.dumps(all_seats), content_type="application/json")