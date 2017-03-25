from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect,render_to_response
from .forms import ViewForm,Acad_details,Add_details,ViewForma
from  student.models import StudentPersonalInfo,StudentAcademicInfo,StudentAdditionalInfo


def index(request):
	id = request.POST.get('student_id')
	if request.method == "POST":
		form = ViewForm(request.POST)
		if form.is_valid():
			StudentPersonalInfo = form.save(commit = False)
			StudentPersonalInfo.save()
			return redirect('acadamicdetails',sid=id)
        
	else:
		form = ViewForm()
	return render(request, "index.html", {'form': form})

def acadamicdetails(request,sid):
	student_details = StudentPersonalInfo.objects.filter(student_id=sid)
	if request.method == "POST":
		formA = Acad_details(request.POST)
		id = request.POST.get('student_id')	
		if formA.is_valid():		
			StudentAcademicInfo = formA.save(commit = False)
			StudentAcademicInfo.save()            
			return redirect('additionaldetails',sid=id)
        
	else:
		formA = Acad_details()
	return render(request, "acadamicdetails.html", {'formA': formA,'id':student_details})

def additionaldetails(request,sid):
	student_details = StudentPersonalInfo.objects.filter(student_id=sid)	
	if request.method == "POST":
		formB = Add_details(request.POST)
		id = request.POST.get('student_id')	
		if formB.is_valid():		
			StudentAdditionalInfo = formB.save(commit = False)
			StudentAdditionalInfo.save()            
			return redirect('success',sid=id)
        
	else:
		formB = Add_details()
	return render(request, "additionaldetails.html", {'formB': formB,'id':student_details})	
	

def success(request,sid):
			try:
				student_details = StudentPersonalInfo.objects.filter(student_id=sid)
				acadamic_details = StudentAcademicInfo.objects.filter(student_id=sid)
				additional_details = StudentAdditionalInfo.objects.filter(student_id=sid)
			except StudentPersonalInfo.DoesNotExist:
				raise Http404("StudentPersonalInfo does not exist")
			return render(request, 'success.html', {'student_details': student_details,'acadamic_details': acadamic_details,'additional_details': additional_details,'id':sid})
	
def editpersonal(request,sid):
	student_details = StudentPersonalInfo.objects.filter(student_id=sid)
	if request.method == "POST":
		form = ViewForm(request.POST)
		if form.is_valid():
			StudentPersonalInfo.objects.filter(student_id=sid).update(student_firstname='aaaa')
			return redirect('success',sid=id)
        
	else:
		form = ViewForma()
	return render(request, "editpersonal.html", {'form':form,'id':student_details})	