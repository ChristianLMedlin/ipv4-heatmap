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