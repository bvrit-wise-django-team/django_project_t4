from django.db import models
	
class StudentPersonalInfo(models.Model):
	student_id = models.CharField(max_length=20,unique=True)
	student_firstname = models.CharField(max_length=50)
	student_lastname = models.CharField(max_length=50)
	student_dob = models.DateField()
	student_address = models.CharField(max_length=2000)
	student_email = models.CharField(max_length=50)
	student_phoneno = models.IntegerField()
 
class StudentAcademicInfo(models.Model):
	program_choices =  ( 
        ('WISE', 'WISE'), 
        ('ATL', 'ATL'),
		('Mission R&D', 'Mission R&D'),
		('Other', 'Other'),	
    )
	student_id = models.CharField(max_length=20,unique=True)
	yearOfJoining = models.IntegerField()
	aggregate = models.IntegerField()
	senior_secondary_institute = models.CharField(max_length=30)
	senior_secondary_board = models.CharField(max_length=30)
	senior_secondary_percentage = models.IntegerField()
	secondary_institute = models.CharField(max_length=30)
	secondary_board = models.CharField(max_length=30)
	secondary_percentage = models.IntegerField()
	program = models.CharField(max_length=30,choices=program_choices,default='Other')
	
class StudentAdditionalInfo(models.Model):
	student_id = models.CharField(max_length=20)
	coacademicactivities = models.CharField(max_length=30)
	details = models.CharField(max_length=2000)