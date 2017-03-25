from django.db import models

# Create your models here.
class JobNotifications(models.Model):
    title = models.CharField(max_length=30)
    notification = models.TextField()
