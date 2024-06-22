from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.
class Booking(models.Model):
    name = models.CharField(max_length=50)
    no_of_guest = models.IntegerField(
        validators=[MaxValueValidator(6), MinValueValidator(1)]
    )
    booking_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Menu(models.Model):
    title = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    inventory = models.IntegerField(validators=[MaxValueValidator(5), MinValueValidator(1)])

    def get_item(self):
        return f'{self.title} : {str(self.price)}'

    def __str__(self):
        return self.title
