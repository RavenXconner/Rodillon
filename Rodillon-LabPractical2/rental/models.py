from django.db import models
from django.contrib.auth import get_user_model
<<<<<<< HEAD
from django.core.validators import MinValueValidator, MaxValueValidator

User = get_user_model()


class TimestampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Car(TimestampedModel):
    name = models.CharField(max_length=100)

    def __str__(self):
        return f'Car: {self.name}'


class RentalLocation(TimestampedModel):
    name = models.CharField(max_length=100)

    def __str__(self):
        return f'Rental Location: {self.name}'


class Rental(TimestampedModel):
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    renter = models.ForeignKey(User, on_delete=models.CASCADE)
    payment = models.CharField(max_length=100)
    sale_price = models.DecimalField(max_digits=7, decimal_places=2) 
    rental_location = models.ForeignKey(RentalLocation, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return f'Rental: {self.car.name} by {self.renter.username} from {self.start_date} to {self.end_date}'


class Review(TimestampedModel):
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    reviewer = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)],
        help_text="Rating must be between 1 and 5"
    )
    comment = models.TextField()

    def __str__(self):
        return f'Review: {self.car.name} by {self.reviewer.username} - Rating: {self.rating}'


class Point(TimestampedModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    points = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.user.username} - Points: {self.points}'
=======

User = get_user_model()

class Car(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
class RentalLocation(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
class Rental(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    renter = models.ForeignKey(User, on_delete=models.CASCADE)
    payment = models.CharField(max_length=100)
    sale_price = models.DecimalField(max_digits=10, decimal_places=2)
    rental_location = models.ForeignKey(RentalLocation, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.car.name} - {self.renter.username}'



class Review(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    reviewer = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField()
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.car.name} - {self.reviewer.username}'
    
class Point(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    points = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.user.username} - {self.points}'
>>>>>>> 7b8546f8a81c77a01bb2664e63606adff273be18
