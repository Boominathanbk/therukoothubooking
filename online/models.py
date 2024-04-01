from django.db import models


class infotech(models.Model):
    firstname = models.CharField(max_length=25)
    secondname = models.CharField(max_length=25)
    mobile1 = models.CharField(max_length=10)
    mobile2 = models.CharField(max_length=10)
    village = models.CharField(max_length=50)
    district = models.CharField(max_length=25)
    total_days = models.IntegerField()
    booking_days = models.DateField("Booking Day (MM/DD/YYYY)")


    def __str__(self):
        return f"{self.firstname} {self.secondname} - Booking on {self.booking_days}"
