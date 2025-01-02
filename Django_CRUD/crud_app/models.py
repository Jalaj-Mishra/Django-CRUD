from django.db import models
# Create your models here.

class EmployeeDetail(models.Model):
    empId = models.IntegerField(primary_key=True)
    empName = models.CharField(max_length=100)
    empEmail = models.EmailField(max_length=100)
    empPassword = models.CharField(max_length=20)


    def __str__(self):
        return f'{self.empName} - {self.empEmail} - {self.empId}'
    