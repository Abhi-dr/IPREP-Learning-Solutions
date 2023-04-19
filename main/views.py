from django.shortcuts import render, redirect
from django.http import HttpResponse
from main.models import Company, Employee

# Create your views here.


def companies_view(request):
    
    companies = Company.objects.all()
    
    parameters = {
        "companies": companies
        }
    
    return render(request, 'companies.html', parameters)

def add_employee(request, id):
    
    employees = Employee.objects.filter(company=None)
    
    parameters = {
        "employees": employees
    }
    
    
    if request.method == "POST":
        employee_id = request.POST.get('employee')
        
        company = Company.objects.get(id=id)
        employee = Employee.objects.get(id=employee_id)
        
        employee.company = company
        
        employee.save()
        
        print("=============================Everything done")
        return redirect("/")
    
    return render(request, "add_employee.html", parameters)