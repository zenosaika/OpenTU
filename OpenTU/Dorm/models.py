from django.db import models
from django.conf import settings

class Room(models.Model):
    room_number = models.CharField(max_length=10)

    def __str__(self):
        return f'{self.room_number}'
    
class Bill(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    room_id = models.ForeignKey(Room, on_delete=models.CASCADE)
    rental_cost = models.FloatField(default=0.0)
    electric_cost = models.FloatField(default=0.0)
    water_cost = models.FloatField(default=0.0)
    payment_status = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.room_id}'