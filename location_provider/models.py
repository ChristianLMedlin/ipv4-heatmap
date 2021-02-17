import csv

from django.db import models

class LocationProvider(models.Model):
    network = models.CharField(max_length=255)
    geoname_id = models.CharField(max_length=255)
    registered_country_geoname_id = models.CharField(max_length=255)
    represented_country_geoname_id = models.CharField(max_length=255)
    is_anonymous_proxy = models.BooleanField()
    is_satellite_provider = models.BooleanField()
    postal_code = models.CharField(max_length=255)
    latitude = models.FloatField()
    longitude = models.FloatField()
    accuracy_radius = models.IntegerField()