from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect,render_to_response
from .forms import ViewForm
from  student.models import StudentContactDetails


def index(request):
    if request.method == "POST":
        form = ViewForm(request.POST) 
        if form.is_valid():		
            StudentContactDetails = form.save(commit = False)
            StudentContactDetails.save()            
            return redirect('success')
        
    else:
        form = ViewForm()
    return render(request, "index.html", {'form': form})


def success(request):
			try:
				student_details = StudentContactDetails.objects.all()
			except StudentContactDetails.DoesNotExist:
				raise Http404("StudentContactDetails does not exist")
			return render(request, 'success.html', {'student_details': student_details})
	
	