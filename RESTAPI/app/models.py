from django.db import models

# Create your models here.
class  Travels(models.Model):
    name = models.CharField(max_length=40)
    source  = models.CharField(max_length=32)
    destination = models.CharField(max_length=32)
    date = models.DateField()
    time = models.TimeField()
    bus_type = models.CharField(max_length=32)
    driver_number = models.BigIntegerField()
    bus_number = models.CharField(max_length=10)
    seats = models.PositiveIntegerField()
    