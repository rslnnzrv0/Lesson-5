from django.db import models


class Car(models.Model):
    make = models.CharField(max_length=100)
    year = models.IntegerField()
    color = models.CharField(max_length=100)
    mileage = models.IntegerField()
    price = models.IntegerField()
