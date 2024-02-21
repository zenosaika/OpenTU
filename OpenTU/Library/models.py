from django.db import models
from django.conf import settings
from User.models import Student
    
class Book(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField()
    quantity = models.SmallIntegerField(default=0)
    borrowers = models.ManyToManyField(Student, blank=True)

    def __str__(self):
        return self.name

class BookTransaction(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    create_date = models.DateField(auto_now_add=True)
    duration = models.SmallIntegerField(default=4)
    address = models.CharField(max_length=70, default='รับเองที่ห้องสมุด')
    is_close = models.BooleanField(default=False)

    def __str__(self):
        return self.book.name[:8]
    
class Room(models.Model):
    name = models.CharField(max_length=15)
    image = models.ImageField()

    def __str__(self):
        return self.name
    
TIME_SLOTS = (
    ('0', '7:30 - 8:30'),
    ('1', '8:30 - 9:30'),
    ('2', '9:30 - 10:30'),
    ('3', '10:30 - 11:30'),
    ('4', '11.30 - 12:30'),
    ('5', '12:30 - 13:30'),
    ('6', '13:30 - 14:30'),
    ('7', '14:30 - 15:30'),
    ('8', '15:30 - 16:30'),
    ('9', '16:30 - 17:30'),
    ('10', '17:30 - 18:30'),
    ('11', '18:30 - 19:30'),
    ('12', '19:30 - 20:30'),
    ('13', '20:30 - 21:30'),
    ('14', '21:30 - 22:30'),
    ('15', '22:30 - 23:30'),
)

class RoomTransaction(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    create_date = models.DateField(auto_now_add=True)
    timeslot = models.CharField(max_length=2, choices=TIME_SLOTS)
    is_close = models.BooleanField(default=False)

    def __str__(self):
        return self.room.name