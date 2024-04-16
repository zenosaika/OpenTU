from django.db import models

class Bus(models.Model):
    name = models.CharField(max_length=60)

    def __str__(self):
        return self.name
    
class Station(models.Model):
    name = models.CharField(max_length=60)
    type = models.CharField(max_length=60)
    available_buses = models.ManyToManyField(Bus, blank=True)

    def __str__(self):
        return self.name