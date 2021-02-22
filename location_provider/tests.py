from django.test import TestCase, Client
from rest_framework.test import APIRequestFactory

from .models import LocationProvider
from .views import LocationProviderViewSet

class TestLocationProvider(TestCase):
    def setUp(self):
        for latitude in range(100):
            for longitude in range(100):
                LocationProvider.objects.create(
                        latitude=latitude + 1, longitude=longitude + 1)

    def test_retrieve_200(self):
        factory = APIRequestFactory()
        view = LocationProviderViewSet.as_view(actions={"get": "retrieve"})
        request = factory.get("/api/locationProvider/")
        response = view(request, pk=1)

        assert response.status_code == 200

    def test_list_200(self):
        factory = APIRequestFactory()
        view = LocationProviderViewSet.as_view(actions={"get": "list"})
        request = factory.get("/api/locationProvider/")
        response = view(request)

        assert response.status_code == 200
        
    def test_list_204(self):
        factory = APIRequestFactory()
        view = LocationProviderViewSet.as_view(actions={"get": "list"})
        request = factory.get("/api/locationProvider/?latRange=1000,2000")
        response = view(request)

        assert response.status_code == 204