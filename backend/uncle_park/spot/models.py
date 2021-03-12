from django.db import models
from users.models import User


class ParkingSpot(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='spots')
    longitude = models.FloatField(blank=True, default=0)
    latitude = models.FloatField(blank=True,  default=0)
    description = models.TextField(default='')
    price = models.CharField(max_length=5)
    image = models.ImageField(upload_to='static', blank=True)
    available = models.BooleanField(default=True)

    def __str__(self):
        return str(self.id) + ' ' + str(self.user.email)
