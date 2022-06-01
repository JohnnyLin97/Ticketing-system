from django.db import models
from Ticketing_System.ticket.custom_fields import SeparatedValuesField
import custom_fields

# Create your models here.

# Transaction record
class TRANSACTION(models.Model):
    transactionId = models.CharField
    name = models.CharField
    phone = models.DecimalField
    email = models.CharField
    seat = SeparatedValuesField()

# Seats of performance
class SEATS(models.Model):
    area = models.CharField(max_length=2) 
    num = models.DecimalField(max_digits=2)
    booked = models.BooleanField
    transactionId = models.ForeignKey(TRANSACTION, on_delete=models.SET_NULL)

