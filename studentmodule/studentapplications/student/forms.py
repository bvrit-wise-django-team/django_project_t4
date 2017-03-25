from django.forms import ModelForm
from student.models import StudentPersonalInfo,StudentAcademicInfo,StudentAdditionalInfo
from django import forms

class ViewForm (forms.ModelForm):
	student_id = forms.CharField(label='ID',max_length=12)
	student_firstname = forms.CharField(label='First Name',max_length=50)
	student_lastname = forms.CharField(label='Last Name',max_length=50)
	student_dob = forms.DateField(label='DOB')
	student_address = forms.CharField(label='Address',widget=forms.Textarea)
	student_email = forms.CharField(label='Email Id',max_length=50)
	student_phoneno = forms.IntegerField(label='Contact Number')
	class Meta :
		model = StudentPersonalInfo
		fields = '__all__'
class Acad_details(forms.ModelForm):
	student_id = forms.CharField(widget = forms.HiddenInput())
	yearOfJoining = forms.IntegerField(label='Year of Joining')
	aggregate = forms.IntegerField()
	senior_secondary_institute = forms.CharField(label='Senior Secondary Institute',max_length=30)
	senior_secondary_board = forms.CharField(label='Senior Secondary Board',max_length=30)
	senior_secondary_percentage = forms.IntegerField(label='Senior Secondary Percentage')
	secondary_institute = forms.CharField(label='Secondary Institute',max_length=30)
	secondary_board = forms.CharField(label='Secondary Board',max_length=30)
	secondary_percentage = forms.IntegerField(label='Secondary Percentage')
	class Meta :
		model = StudentAcademicInfo
		fields = '__all__'
		
class Add_details(forms.ModelForm):
	student_id = forms.CharField(widget = forms.HiddenInput())
	coacademicactivities = forms.CharField(label='Co-Acadamic Activities',max_length=30)
	details = forms.CharField(label='Description',widget=forms.Textarea)
	class Meta :
		model = StudentAdditionalInfo
		fields = '__all__'

class ViewForma (forms.ModelForm):
	student_id = forms.CharField(label='ID',max_length=12)
	student_firstname = forms.CharField(label='First Name',max_length=50)
	student_lastname = forms.CharField(label='Last Name',max_length=50)
	student_dob = forms.DateField(label='DOB')
	student_address = forms.CharField(label='Address',widget=forms.Textarea)
	student_email = forms.CharField(label='Email Id',max_length=50)
	student_phoneno = forms.IntegerField(label='Contact Number')
	class Meta :
		model = StudentPersonalInfo
		fields = '__all__'		

