from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from location_provider.views import LocationProviderViewSet

router = routers.DefaultRouter()
router.register('locationProvider', LocationProviderViewSet, "locationProvider")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls))
]
