from django.db import models
from flights.models import Flight

# Create your models here.
class Reservation(models.Model):

    flight = models.ForeignKey(Flight, on_delete=models.PROTECT)
    num_people = models.IntegerField()
    total_cost = models.DecimalField(max_digits=10, decimal_places=2)

class Ticket(models.Model):

    # Ticket_Class designation
    FIRST_CLASS = 'F'
    BUSINESS_CLASS = 'B'
    MAIN_CABIN = "M"

    TICKET_CLASS_CHOICES = [
        (FIRST_CLASS, "first_class"),
        (BUSINESS_CLASS, "business_class"),
        (MAIN_CABIN, "main_cabin"),

    ]
    reservation = models.ForeignKey(Reservation, on_delete=models.PROTECT)
    seat = models.CharField(max_length=10)
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    ticket_class = models.CharField(
        max_length=1,
        choices=TICKET_CLASS_CHOICES
    )
