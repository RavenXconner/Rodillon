from django.contrib import admin
from .models import Car, RentalLocation, Rental, Review, Point

admin.site.register(Car)
admin.site.register(RentalLocation)
admin.site.register(Rental)
admin.site.register(Review)
admin.site.register(Point)


# Register your models here.
