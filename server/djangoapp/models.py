# Uncomment the following imports before adding the Model code

from django.db import models
from django.utils.timezone import now
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.

class CarMake(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name


class CarModel(models.Model):
    car_make = models.ForeignKey(CarMake, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    CAR_TYPES = [
        ('COMPACT', 'Compact'),
        ('SEDAN', 'Sedan'),
        ('WAGON', 'Wagon'),
        ('SUV', 'SUV'),
        ('TRUCK', 'Truck'),
    ]
    type = models.CharField(max_length=10, choices=CAR_TYPES, default='COMPACT')
    year = models.IntegerField(default=2023,
        validators=[
            MaxValueValidator(2023),
            MinValueValidator(2015)
        ])

    COLORS = [
        ('BLACK', 'Black'),
        ('WHITE', 'White'),
        ('BLUE', 'Blue'),
        ('RED', 'Red'),
        ('GREEN', ' Green'),
        ('YELLOW', 'Yellow'),
    ]
    color = models.CharField(max_length=10, choices=COLORS, default='BLACK')

    SHADES = [
        ('', '------'),
        ('LIGHT', 'Light'),
        ('DARK', 'Dark')
    ]

    shade = models.CharField(max_length=10, choices=SHADES, default='', blank=True)

    def __str__(self):
        return self.name
# - __str__ method to print a car make object
