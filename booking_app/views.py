from django.shortcuts import render, redirect
from django.contrib import messages
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
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        check_in = request.POST.get('check_in')
        check_out = request.POST.get('check_out')
        
        existing_booking = Booking.objects.filter(apartment=apartment, check_in__lt=check_out,
                                                   check_out__gt=check_in)
        if existing_booking.exists():
            messages.error(request, 'This apartment is already booked for the selected dates.')
        else:
        
            booking = Booking.objects.create(
                apartment=apartment,
                user = request.user,
                name = name,
                email = email,
                phone = phone,
                check_in = check_in,
                check_out = check_out
            )
            return redirect('booking_confirmation', id=booking.id)
            
    return render(request, 'booking_page.html', {'apartment': apartment})

@login_required
def booking_confirmation(request, id):
    booking = Booking.objects.get(id=id)
    return render(request, 'reservation_success.html', {'booking': booking})

