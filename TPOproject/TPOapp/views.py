from django.shortcuts import render,redirect
from .models import JobNotifications
from django.http import HttpResponse, HttpResponseRedirect
from .forms import JobNotificationsForm
from django.shortcuts import get_object_or_404, render


# Create your views here.
def tpo_dashboard(request):
    if request.method == "POST":
        form = JobNotificationsForm(request.POST)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect('/tpo/dashboard/')
    notifications = JobNotifications.objects.all()
    form = JobNotificationsForm()
    return render(request, 'add_notification.html', {"form": form, "notifications": notifications})

