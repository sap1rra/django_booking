from django.shortcuts import render
from .models import  Apartment, Booking
# Create your views here.
def home(request):
    apartments = Apartment.objects.filter(is_available=True)
    return render(request, 'home.html', {'apartments': apartments})


def apartment_page(request, id):
    apartment = Apartment.objects.get(id=id)
    return render(request, 'apartment_page.html', {'apartment': apartment})
