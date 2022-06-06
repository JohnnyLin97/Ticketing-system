from .models import Event1_seats
import random
from django.core import serializers

def create_seat_table():
    for i in range(1,21):

        seatId = random.randrange(100000000000,999999999999)
        area = 'J'
        num = str(i)
        booked = False
        transactionId = ''

        unit = Event1_seats.objects.create(
            id = seatId,
            area = area,
            num = num,
            booked = booked,
            transactionId = transactionId
        )
        
        unit.save()

def retrieve_all_seats():
    all_units = Event1_seats.objects.all()

    #Convert querySet to list
    all_units_list = list(all_units)

    all_seats = []
    for i in all_units_list:
        all_seats.append(unit_to_dic(i))

    return all_seats

def unit_to_dic(unit):
    dict = {}
    dict['id'] = unit.id
    dict['area'] = unit.area
    dict['num'] = unit.num
    dict['transactionId'] = unit.transactionId

    if unit.booked:
        dict['booked'] = True
    else:
        dict['booked'] = False

    return dict