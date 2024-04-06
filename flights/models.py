from django.db import models

class Flight(models.Model):
    flight_number = models.CharField(max_length=10)
    airways_name = models.CharField(max_length=50)
    departure_time = models.DateTimeField()
    ticket_price = models.DecimalField(max_digits=9, decimal_places=2)

    def __str__(self):
        return f"{self.flight_number} - {self.airways_name}"


# Create your models here.
