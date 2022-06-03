from django.db import models

# Create your models here.

# Transaction record
class TRANSACTION(models.Model):
    transactionId = models.CharField
    name = models.CharField
    phone = models.DecimalField
    email = models.CharField
    

# Seats of performance
class SEATS(models.Model):
    id = models.CharField(max_length=45).primary_key
    area = models.CharField(max_length=1) 
    num = models.CharField(max_length=2)
    booked = models.BooleanField
    transactionId = models.CharField(max_length=45)