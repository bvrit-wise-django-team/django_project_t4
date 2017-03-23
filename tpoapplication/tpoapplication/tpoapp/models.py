from django.db import models
from django.utils import timezone

# Create your models here.
class Drive(models.Model):
	drive_name = models.CharField(max_length=255)
	drive_date = models.DateTimeField(default=timezone.now)
