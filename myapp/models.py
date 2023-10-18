from django.db import models

# Create your models here.

class User(models.Model):
    email = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255)

class Location(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)
    email = models.CharField(max_length=255)
    website = models.CharField(max_length=255)
    latitude = models.FloatField()
    longitude = models.FloatField()

class Sport(models.Model):
    name = models.CharField(max_length=255)

class Facility(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    location = models.ForeignKey(Location, related_name='facilities', on_delete=models.CASCADE)
    sport = models.ForeignKey(Sport, related_name='facilities', on_delete=models.CASCADE)
