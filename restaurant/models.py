from django.db import models
from decimal import Decimal
from django.utils import timezone


# Create your models here.
class Booking(models.Model):
    first_name = models.CharField(max_length=200)
    reservation_date = models.DateField()
    bookingDate = models.DateField(default=timezone.now)
    reservation_slot = models.SmallIntegerField(default=10)
    no_of_guests = models.SmallIntegerField(default=1)
    name = models.CharField(max_length=200, default="Unknown")

    def __str__(self):
        # return self.first_name
        return f"{self.name} @ {self.reservation_date} for {self.no_of_guests} guests"


class Menu(models.Model):
    name = models.CharField(max_length=200)
    # price = models.IntegerField(null=False)
    price = models.DecimalField(max_digits=6, decimal_places=2, default=Decimal("0.00"))
    menu_item_description = models.TextField(max_length=1000, default="")
    title = models.CharField(max_length=200, default="Untitled")
    inventory = models.IntegerField(default=0)

    # def __str__(self):
    #     # return self.name
    #     return self.title

    def __str__(self):
        return f"{self.title} : {str(self.price)}"
