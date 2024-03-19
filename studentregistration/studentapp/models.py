from django.db import models

# Create your models here.
class Student(models.Model):
    name=models.CharField(max_length=50)
    address=models.CharField(max_length=100)
    course=models.CharField(max_length=50)
    email=models.EmailField(max_length=50)
    password=models.CharField(max_length=50)
    attendance=models.CharField(max_length=50)
    marks=models.CharField(max_length=50)
    