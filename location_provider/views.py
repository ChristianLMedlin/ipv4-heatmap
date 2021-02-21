from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.response import Response

from .serializers import LocationProviderSerializer, LatLongOnlySerializer
from .models import LocationProvider


class LocationProviderViewSet(viewsets.ViewSet):
    def retrieve(self, request, pk=None):
        queryset = LocationProvider.objects.all()
        location_data = get_object_or_404(queryset, pk=pk)
        serializer = LocationProviderSerializer(location_data)

        return Response(serializer.data)

    def list(self, request):
        queryset = LocationProvider.objects.all()
        query = request.query_params
        # Check if either latRange or longRange are in query_marams.
        # If they are, filter the queryset based on the value ranges provided.
        if "latRange" in query:
            low_lat, high_lat = query["latRange"].split(",")
            queryset = queryset.filter(
                    latitude__range=(low_lat, high_lat))
        if "longRange" in query:
            low_long, high_long = query["longRange"].split(",")
            queryset = queryset.filter(
                    longitude__range=(low_long, high_long))
        # Limit large calls to 20,000 objects to reduce latency.
        queryset = queryset[:20000]

        # If latLongOnly is True, the serializer will only return latitude and 
        # longitude in the response.
        if "latLongOnly" in query:
            if query["latLongOnly"].lower() == "true":
                serializer = LatLongOnlySerializer(queryset, many=True)
        else:
            serializer = LocationProviderSerializer(queryset, many=True)

        return Response(serializer.data)
