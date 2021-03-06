from unittest.util import _MAX_LENGTH
from django.db import models
from django_mysql.models import ListCharField

# Create your models here.

# Transaction record
class Transaction(models.Model):
    transactionId = models.CharField(max_length=45).primary_key
    name = models.CharField(max_length=45)
    phone = models.CharField(max_length=45)
    email = models.CharField(max_length=45)
    seat = ListCharField(
        base_field = models.CharField(max_length=10),
        size = 4,
        max_length = (4*45)
    )
    

# Seats of performance
class Event1_seats(models.Model):
    seatId = models.CharField(max_length=10).primary_key
    area = models.CharField(max_length=1) 
    num = models.CharField(max_length=2)
    booked = models.BooleanField(default=False)
    transactionId = models.CharField(max_length=45)