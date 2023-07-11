from django.db import models

class Employee(models.Model):
    Emp_name = models.CharField(max_length=50)
    Company = models.CharField(max_length=50)
    city = models.CharField(max_length=50)