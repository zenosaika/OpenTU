from django.db import models
from User.models import Student
    
class Book(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField()
    quantity = models.SmallIntegerField(default=0)
    borrowers = models.ManyToManyField(Student, blank=True)

    def __str__(self):
        return self.name
