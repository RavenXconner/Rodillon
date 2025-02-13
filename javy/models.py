from django.db import models
from django.contrib.auth.models import User

class Vehicle(models.Model):
    TYPE_CHOICES = [('Sedan', 'Sedan'), ('SUV', 'SUV'), ('Luxury', 'Luxury')]
    FUEL_CHOICES = [('Petrol', 'Petrol'), ('Diesel', 'Diesel'), ('Electric', 'Electric')]

    make = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    vehicle_type = models.CharField(max_length=10, choices=TYPE_CHOICES)
    fuel_type = models.CharField(max_length=10, choices=FUEL_CHOICES)
    price_per_day = models.DecimalField(max_digits=6, decimal_places=2)
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.make} {self.model}"
 
class Booking(models.Model):
    PAYMENT_STATUS_CHOICES = [('Successful', 'Successful'), ('Failed', 'Failed')]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    pickup_date = models.DateTimeField()
    dropoff_date = models.DateTimeField()
    location = models.CharField(max_length=100)
    total_price = models.DecimalField(max_digits=7, decimal_places=2)
    payment_status = models.CharField(max_length=10, choices=PAYMENT_STATUS_CHOICES)

    def __str__(self):
        return f"Booking for {self.user.username} - {self.vehicle}"

class Payment(models.Model):
    booking = models.OneToOneField(Booking, on_delete=models.CASCADE)
    payment_method = models.CharField(max_length=20)
    amount = models.DecimalField(max_digits=7, decimal_places=2)
    status = models.CharField(max_length=10)

    def __str__(self):
        return f"Payment of {self.amount} for booking {self.booking.id}"

class Review(models.Model):
    booking = models.OneToOneField(Booking, on_delete=models.CASCADE)
    rating = models.IntegerField()
    comment = models.TextField()

    def __str__(self):
        return f"Review for booking {self.booking.id}"

class LoyaltyProgram(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    points_earned = models.IntegerField()
    discounts_applied = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f"Loyalty Program for {self.user.username}"
