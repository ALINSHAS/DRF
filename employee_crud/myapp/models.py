from django.db import models

class Employee(models.Model):
    empid=models.IntegerField()
    name=models.CharField(max_length=30)
    age=models.IntegerField()
    place=models.CharField(max_length=30)
    gender_choices=[
        ('male','Male'),('female','Female')  #dbvalue,displayvalue
    ]
    gender=models.CharField(max_length=20,choices=gender_choices)
    joining_date=models.DateField()
    # joining_date=models.DateField(auto_now_add=True)
    salary=models.IntegerField()
    designation=models.CharField(max_length=30)
    image=models.ImageField(upload_to="myapp",null=True)