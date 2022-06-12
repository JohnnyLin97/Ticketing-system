import email
from .models import Event1_seats
from django.http import HttpResponse, HttpResponseForbidden, HttpResponseNotAllowed, HttpResponseNotFound
import json
from .db_helper import book_seat, check_seat_state, get_transaction_db, retrieve_all_seats, create_transaction_db, retrieve_all_transactions

# Create your views here.
def retrieve_seats(request):
    try:
        all_seats = retrieve_all_seats()
    
    except Exception as e: 
        print(e)

    return HttpResponse(json.dumps(all_seats), content_type="application/json")


def get_transaction(request):
    if request.method == "POST": 
        transaction_id = json.loads(request.body)["id"]
        
        try:
            transaction = get_transaction_db(transaction_id)
            return HttpResponse(json.dumps(transaction), content_type="application/json")
        
        except Exception as e:
            print(e)
            return HttpResponseNotFound(json.dumps("Can't find the transaction"), content_type="application/json")

    else:
        return HttpResponseForbidden()

def create_transaction(request):
    if request.method == "POST": 
        request_json = json.loads(request.body)

        email = request_json["email"]
        name = request_json["name"]
        phone = request_json["phone"]
        seat = request_json["seat"]

        if check_seat_state(seat):
            return HttpResponseNotFound(json.dumps("Seat is already reserved"), content_type="application/json")

        id = create_transaction_db(email, name, phone, seat)
        dict = {}
        dict['id'] = id

        book_seat(seat, id)

        return HttpResponse(json.dumps(dict), content_type="application/json")

    else:
        return HttpResponseForbidden()


def retrieve_transaction(request):
    try:
        all_transactions = retrieve_all_transactions()
    
    except Exception as e: 
        print(e)

    return HttpResponse(json.dumps(all_transactions), content_type="application/json")