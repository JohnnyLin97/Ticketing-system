from .models import Event1_seats, Transaction
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
        all_seats.append(unit_to_dic_seats(i))

    return all_seats

def get_transaction_db(transaction_id):
    unit = Transaction.objects.filter(id = transaction_id)
    unit_list = list(unit)
    return unit_to_dic_transaction(unit_list[0])

def create_transaction_db(email, name, phone, seat):
    id = random.randrange(100000000000,999999999999)
    
    unit = Transaction.objects.create(
            id = id,
            email = email,
            name = name,
            phone = phone,
            seat = seat
    )

    unit.save()

    return id
    

def unit_to_dic_seats(unit):
    dict = {}
    dict['id'] = unit.id
    dict['area'] = unit.area
    dict['num'] = unit.num
    dict['transactionId'] = unit.transactionId
    dict['booked'] = unit.booked

    return dict

def unit_to_dic_transaction(unit):
    dict = {}
    dict['id'] = unit.id
    dict['email'] = unit.email
    dict['name'] = unit.name
    dict['phone'] = unit.phone
    dict['seat'] = unit.seat

    return dict