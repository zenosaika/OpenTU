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

class Transaction(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    create_date = models.DateField(auto_now_add=True)
    duration = models.SmallIntegerField(default=4)
    address = models.CharField(max_length=70, default='รับเองที่ห้องสมุด')
    is_close = models.BooleanField(default=False)

    def __str__(self):
        return self.book.name[:8]