from django.urls import path
from .  import views

urlpatterns = [
    path('', views.home, name='home'),
    path('apartment/<int:id>/', views.apartment_page, name='apartment_page'),
    path('booking/<int:id>/', views.booking_page, name='booking_page'),
    path('booking/confirmation/<int:id>/', views.booking_confirmation, name='booking_confirmation')
]
