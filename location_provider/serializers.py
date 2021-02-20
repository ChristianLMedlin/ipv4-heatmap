from rest_framework import serializers

from .models import LocationProvider

class LocationProviderSerializer(serializers.ModelSerializer):
    class Meta:
        model = LocationProvider
        fields = ("id", "latitude", "longitude", "accuracy_radius")

class LatLongOnlySerializer(serializers.ModelSerializer):
    class Meta:
        model = LocationProvider
        fields = ("latitude", "longitude")