from django.db import models


class Car(models.Model):
    category = models.CharField(max_length=44)
    marka = models.CharField(max_length=33)
    model = models.CharField(max_length=33)
    price = models.PositiveIntegerField()
    year = models.PositiveSmallIntegerField()
    mileage = models.PositiveIntegerField()
    city = models.CharField(max_length=44)
    country = models.CharField(max_length=33)
    with_photo = models.BooleanField()
    color = models.CharField(max_length=33)
    volume = models.FloatField()
    description = models.TextField()


class Bet(models.Model):
    number = models.IntegerField()
    total_number = models.IntegerField()
    buy_now = models.IntegerField()
    start_date = models.DateField
    end_date = models.DateField()