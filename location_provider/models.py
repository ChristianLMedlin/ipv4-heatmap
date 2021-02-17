import csv

from django.db import models

class LocationProvider(models.Model):
    network = models.CharField(max_length=255)
    geoname_id = models.IntegerField(null=True)
    registered_country_geoname_id = models.IntegerField(null=True)
    represented_country_geoname_id = models.IntegerField(null=True)
    is_anonymous_proxy = models.BooleanField(null=True)
    is_satellite_provider = models.BooleanField(null=True)
    postal_code = models.CharField(null=True, max_length=255)
    latitude = models.FloatField(null=True)
    longitude = models.FloatField(null=True)
    accuracy_radius = models.IntegerField(null=True)