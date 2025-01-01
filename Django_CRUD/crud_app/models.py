from django.db import models
# Create your models here.

class EmployeeDetails(models.Model):
    empId = models.AutoField(primary_key=True)
    empName = models.CharField(max_length=100)
    empEmail = models.EmailField(max_length=100)
    empPassword = models.CharField(max_length=20)