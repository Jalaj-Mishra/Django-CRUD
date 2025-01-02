from django.shortcuts import render
from .models import EmployeeDetail
from .forms import AddEmployee
# Create your views here.
def home(request):
    if request.method == 'GET':
        details = EmployeeDetail.objects.all()
        return render(request, 'index.html', {'details': details})
    else:
        return render(request, 'index.html')



def addEmployee(request):
    if request.method == 'POST':
        form = AddEmployee(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index.html') 
    else:
        form = AddEmployee()
        print(form)
    return render(request, "addEmployee.html", {"form": form})