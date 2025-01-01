from django import forms
from .models import EmployeeDetails
class AddEmployee(forms.ModelForm):
    
    class Meta:
        model = EmployeeDetails
        fields = ['empId', 'empName', 'empEmail', 'empPassword']

    # class Meta():
    #     empId = forms.IntegerField(label='empId', max_value=5)
    #     empName = forms.CharField(label="EmpName", max_length=20),
    #     empEmail = forms.EmailField(label="EmpEmail"),
    #     empPassword = forms.CharField(label="EmpPassword", max_length=20, widget=forms.PasswordInput)