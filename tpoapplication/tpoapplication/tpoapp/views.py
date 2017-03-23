from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import ViewForm
from  tpoapp.models import Comment


def next(request):
    if request.method == "POST":
        form = ViewForm(request.POST)
        if form.is_valid():
            Drive = form.save(commit = False)
            Drive.save()
            
            return redirect('success')
        
    else:
        form = ViewForm()
    return render(request, "next.html", {'form': form})


def success(request):
    return HttpResponse('Success! Notifications Updated.')

def display(request):
         try:
             Drives = Drive.objects.all()
         except Drive.DoesNotExist:
             raise Http404("Comment does not exist")
            
         return render(request, "display.html",{'Drives': Drives})