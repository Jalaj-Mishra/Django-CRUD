from django.db import models
# Create your models here.

class EmployeeDetails(models.Model):
    employee_id = models.AutoField(primary_key=True)
    employee_name = models.CharField(max_length=100)
    employee_email = models.EmailField(max_length=100)
    employee_phone = models.CharField(max_length=20)