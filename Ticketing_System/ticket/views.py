from .models import Event1_seats
from django.http import HttpResponse
import json

# Create your views here.
def retrieve(request):
    try:
        #unit = Event1_seats.objects.get(id = 5494156464648)
        unit = Event1_seats.objects.get(booked=False)
        print(unit)
        '''
        seatId = 549415637700
        area = 'A'
        num = '1'
        booked = False
        transactionId = ''
        unit = Event1_seats.objects.create(
            id = seatId,
            area = area,
            num = num,
            booked = booked,
            transactionId = transactionId
        )
        unit.save()'''
    
    except Exception as e: 
        print(e)

    response_data = {}
    response_data['result'] = 'error'
    response_data['message'] = 'Some error message'

    return HttpResponse(json.dumps(response_data), content_type="application/json")