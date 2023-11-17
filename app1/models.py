from django.db import models
from django.contrib.auth.models import User

class Course (models.Model):
    course_name=models.CharField(max_length=255) 
    fee=models.IntegerField()
   

class Student (models.Model):
    course=models.ForeignKey(Course,on_delete=models.CASCADE)
    student_name=models.CharField(max_length=255) 
    address=models.CharField(max_length=255,default='Unknown')
    age=models.IntegerField()
    joining_date=models.DateField()


class Teacher(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course=models.ForeignKey(Course,on_delete=models.CASCADE)
    age = models.IntegerField()
    address = models.CharField(max_length=255)
    contact_number = models.CharField(max_length=15)
    photo = models.ImageField(upload_to='teacher_photos/')

    
