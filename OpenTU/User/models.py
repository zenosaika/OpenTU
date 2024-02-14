from django.db import models
from django.conf import settings
from Course.models import Course

class Student(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    student_id = models.CharField(max_length=10)
    email = models.EmailField()
    image = models.ImageField(blank=True)
    enrolled_courses = models.ManyToManyField(Course, blank=True)

    def __str__(self):
        return self.student_id
