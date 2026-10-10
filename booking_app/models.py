from django.db import models

class Hotel(models.Model):
    name = models.CharField(max_length=150)
    location = models.CharField(max_length=150)
    description = models.TextField()

    def __str__(self):
        return self.name
    
    
class Apartment(models.Model):
    APARTAMENT_TYPES = [
        ('studio', 'Studio'),
        ('one_bedroom', 'One Bedroom'),
        ('two_bedroom', 'Two Bedroom'),
        ('penthouse', 'Penthouse'),
    ]
    
    name = models.CharField(max_length=150)
    location = models.CharField(max_length=150)
    description = models.TextField(null=True, blank=True)
    price_per_night = models.DecimalField(max_digits=8, decimal_places=2)
    capacity = models.IntegerField(default=1)
    image =  models.ImageField(upload_to='apartments/', null=True, blank=True)
    type_apartment = models.CharField(max_length=50, choices=APARTAMENT_TYPES, default='one_bedroom')
    is_available = models.BooleanField(default=True)
    
    def __str__(self):
        return self.name
    
class Meta:
        verbose_name = "Apartment"
        verbose_name_plural = "Apartments"
        ordering = ['is_available', 'name']
        
        
class Booking(models.Model):
    STATUS_CHOISES = [
        ('pending', 'Pending'),
        ('confirmed', 'Confirmed'),
        ('cancelled', 'Cancelled'),
    ]
   
    apartment = models.ForeignKey(Apartment, on_delete=models.CASCADE)
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    check_in = models.DateField()
    check_out = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOISES, default='pending')

    def __str__(self):
        return f"Booking {self.id} - {self.apartment.name} - {self.user.username}"