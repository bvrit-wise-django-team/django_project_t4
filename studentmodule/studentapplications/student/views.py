from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect,render_to_response
from .forms import ViewForm,Acad_details,Add_details
from  student.models import StudentPersonalInfo,StudentAcademicInfo,StudentAdditionalInfo


def index(request):
    if request.method == "POST":
        form = ViewForm(request.POST) 
        if form.is_valid():		
            StudentPersonalInfo = form.save(commit = False)
            StudentPersonalInfo.save()            
            return redirect('acadamicdetails')
        
    else:
        form = ViewForm()
    return render(request, "index.html", {'form': form})

def acadamicdetails(request):
    if request.method == "POST":
        formA = Acad_details(request.POST) 
        if formA.is_valid():		
            StudentAcademicInfo = formA.save(commit = False)
            StudentAcademicInfo.save()            
            return redirect('additionaldetails')
        
    else:
        formA = Acad_details()
    return render(request, "acadamicdetails.html", {'formA': formA})

def additionaldetails(request):
    if request.method == "POST":
        formB = Add_details(request.POST) 
        if formB.is_valid():		
            StudentAdditionalInfo = formB.save(commit = False)
            StudentAdditionalInfo.save()            
            return redirect('success')
        
    else:
        formB = Add_details()
    return render(request, "additionaldetails.html", {'formB': formB})	
	

def success(request):
			try:
				student_details = StudentPersonalInfo.objects.all()
				acadamic_details = StudentAcademicInfo.objects.all()
				additional_details = StudentAdditionalInfo.objects.all()
			except StudentPersonalInfo.DoesNotExist:
				raise Http404("StudentPersonalInfo does not exist")
			return render(request, 'success.html', {'student_details': student_details,'acadamic_details': acadamic_details,'additional_details': additional_details})
	
	