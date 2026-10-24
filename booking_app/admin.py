from django.contrib import admin

# Register your models here.
from .models import Booking, Apartment, Hotel
admin.site.register(Booking)
admin.site.register(Apartment)
admin.site.register(Hotel)