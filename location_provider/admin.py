from django.contrib import admin

from .models import LocationProvider

class LocationProviderAdmin(admin.ModelAdmin):
    list_display = [field.name for field in LocationProvider._meta.fields]

admin.site.register(LocationProvider, LocationProviderAdmin)