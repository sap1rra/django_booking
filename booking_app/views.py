from django.shortcuts import render
from .models import  Apartment, Booking
from django.contrib.auth.decorators import login_required


def home(request):
    apartments = Apartment.objects.filter(is_available=True)
    return render(request, 'home.html', {'apartments': apartments})


def apartment_page(request, id):
    apartment = Apartment.objects.get(id=id)
    return render(request, 'apartment_page.html', {'apartment': apartment})


@login_required
def booking_page(request, id):
    apartment = Apartment.objects.get(id=id)
    return render(request, 'booking_page.html', {'apartment': apartment})

