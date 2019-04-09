from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm, CompanyForm, RoleTypeForm, EmployeeForm, RoleLogForm
from django.contrib.auth import login, authenticate
from django.urls import reverse_lazy
from django.views import generic
from django.contrib import messages
from .models import Company, Profile, Role_Type, Employee, Role_Log
from .script import get_employee_roles
# Create your views here.

def sign_up(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            profile= Profile.objects.create(user = user)
            login(request, user)
            return redirect('company_create', pk=profile.pk)
    else:
        form = CustomUserCreationForm()
    return render(request, 'signup.html', {'form': form})

def create_company(request, pk):
    user = request.user
    if request.method == 'POST':
        form = CompanyForm(request.POST)
        if form.is_valid():
            company = form.save()
            Profile.objects.filter(pk=pk).update(company=company)
            return redirect('/')
    else:
        form = CompanyForm()
    return render(request, 'create_company.html', {'form': form, 'user':user})

def company_detail(request, pk):
    company = Company.objects.get(pk=pk)
    form = RoleTypeForm(request.POST)
    if form.is_valid():
        role = form.save(commit=False)
        role.company = company
        role.save()
        return redirect(request.path)
    else:  # 5
        # Create an empty form instance
        form = RoleTypeForm()
    return render(request, 'company_detail.html', {'company': company, 'form': form, })

def employee_list(request):
    pk = request.user.profile.company.pk
    company = Company.objects.get(pk=pk)
    employees = Employee.objects.all().filter(company=company)
    return render(request, 'active_employee_list.html', {'employees': employees})

def create_employee(request):
    pk = request.user.profile.company.pk
    company = Company.objects.get(pk=pk)
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            employee = form.save(commit = False)
            employee.company = company
            employee.save()
            return redirect('employee_list')
    else:
        form = EmployeeForm()
    return render(request, 'create_employee.html', {'form': form})

def edit_role_log(request, pk):
    employee = Employee.objects.get(pk=pk)
    if request.method == 'POST':
        form = RoleLogForm(request.POST)
        if form.is_valid():
            role_log = form.save(commit = False)
            role_log.employee = employee
            role_log.company = employee.company
            role_log.save()
            return redirect('employee_list')
    else: 
        form = RoleLogForm(request.POST)
    return render(request, 'role_log_edit.html', {'form': form, 'employee': employee})

def employee_detail(request, pk):
    employee = Employee.objects.get(pk=pk)
    roles = get_employee_roles(employee)
    return render(request, 'employee_detail.html', {'roles': role, 'employee': employee})
