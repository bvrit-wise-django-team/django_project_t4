from django.forms import ModelForm
from django import forms
from .models import JobNotifications

class JobNotificationsForm(ModelForm):
    class Meta:
        model = JobNotifications
        fields = '__all__'