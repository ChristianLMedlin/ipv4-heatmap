from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.response import Response

from .serializers import LocationProviderSerializer
from .models import LocationProvider


class LocationProviderViewSet(viewsets.ViewSet):
    def retrieve(self, request, pk=None):
        queryset = LocationProvider.objects.all()
        location_data = get_object_or_404(queryset, pk=pk)
        serializer = LocationProviderSerializer(location_data)

        return Response(serializer.data)

    def list(self, request):
        queryset = LocationProvider.objects.all()
        #serializer = LocationProviderSerializer(queryset, many=True)
        query = request.query_params
        if "bottomLat" in query and "topLat" in query:
            queryset = queryset.filter(
                    latitude__range=(query["bottomLat"], query["topLat"]))
        if "bottomLong" in query and "topLong" in query:
            queryset = queryset.filter(
                    longitude__range=(query["bottomLong"], query["topLong"]))
        serializer = LocationProviderSerializer(queryset, many=True)

        return Response(serializer.data)
