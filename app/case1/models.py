from django.db import models

# Create your models here.


class Vehicle(models.Model):
    plate = models.CharField(max_length=20)


class NavigationRecord(models.Model):
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    datetime = models.DateTimeField(auto_now_add=True, blank=True)
    latitude = models.FloatField()
    longitude = models.FloatField()