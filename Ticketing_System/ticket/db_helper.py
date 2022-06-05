

from Ticketing_System.ticket.models import Event1_seats


def search_seats(col_name, keyword):
    unit = Event1_seats.objects.get(col_name = keyword)

    unit = Event1_seats.objects.all