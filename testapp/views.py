'''Name :- Vijay Sahebrao Patil
   Roll :- 57
   Class :- TE IT
                             '''



import imp
from django.shortcuts import redirect, render
from testapp.forms import EmployeeForm
from testapp.models import Employee

# Create your views here.

#Select Operation
def retrive_view(request):
    employees = Employee.objects.all()
    return render(request, 'testapp/index.html',{'employees':employees})

#Insert Operation
def create_view(request):
    form = EmployeeForm()
    if request.method == 'POST':
        form = EmployeeForm(request.POST) #get the data from the form and save to the database.after that display home page 
        if form.is_valid():
            form.save()
        return redirect('/')
    return render(request, 'testapp/create.html', {'form':form})

def delete_view(request,id):
    employee = Employee.objects.get(id=id)
    employee.delete()
    return redirect('/')

def update_view(request,id):
    employee = Employee.objects.get(id=id)
    if request.method == 'POST':
        form = EmployeeForm(request.POST,instance=employee)
        if form.is_valid():
            form.save()
        return redirect('/')
    return render(request, 'testapp/update.html',{'employee':employee})