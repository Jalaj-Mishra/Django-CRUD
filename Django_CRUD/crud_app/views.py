from django.shortcuts import render
from .models import EmployeeDetails

# Create your views here.
def home(request):
    if request.method == 'GET':
        details = EmployeeDetails.objects.all()
        return render(request, 'index.html', {'details': details})
    else:
        return render(request, 'index.html')