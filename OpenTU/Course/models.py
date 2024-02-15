from django.db import models

DAYS_OF_WEEK = (
    ('0', 'Monday'),
    ('1', 'Tuesday'),
    ('2', 'Wednesday'),
    ('3', 'Thursday'),
    ('4', 'Friday'),
    ('5', 'Saturday'),
    ('6', 'Sunday'),
)

class Course(models.Model):
    short_name = models.CharField(max_length=5)
    full_name = models.CharField(max_length=255)
    credit = models.SmallIntegerField()
    section = models.CharField(max_length=6)
    class_day = models.CharField(max_length=1, choices=DAYS_OF_WEEK)
    class_start = models.TimeField()
    class_finish = models.TimeField()
    room = models.CharField(max_length=10)

    def __str__(self):
        return f'{self.short_name}_{self.section}'
