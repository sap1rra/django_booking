from django.urls import path
from .  import views

urlpatterns = [
    path('', views.home, name='home'),
    path('apartment/<int:id>/', views.apartment_page, name='apartment_page'),
]
