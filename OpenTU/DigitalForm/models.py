from django.db import models
from django.conf import settings

class Report(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    header = models.CharField(max_length=60)
    body = models.TextField()
    files = models.FileField(blank=True, null=True)
    status = models.CharField(max_length=10, default='Pending')

    def __str__(self):
        return self.header[:10]
