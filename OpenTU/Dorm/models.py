from django.db import models

class Room(models.Model):
    room_number = models.CharField(max_length=10)

    def __str__(self):
        return f'{self.room_number}'
    
class Bill(models.Model):
    room_id = models.ForeignKey(Room, on_delete=models.CASCADE)
    electric_cost = models.FloatField(default=0.0)
    water_cost = models.FloatField(default=0.0)
    payment_status = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.room_id}'