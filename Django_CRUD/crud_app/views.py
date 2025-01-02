from django.shortcuts import render, redirect
from .models import EmployeeDetail
from .forms import AddEmployee
# Create your views here.
def home(request):
    if request.method != 'GET':
        return render(request, 'index.html')
    details = EmployeeDetail.objects.all()
    return render(request, 'index.html', {'details': details})



def addEmployee(request):
    if request.method == 'POST':
        form = AddEmployee(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index.html') 
    else:
        print("get request")
        form = AddEmployee()
    return render(request, "addEmployee.html", {"form": form})