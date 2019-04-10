from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm, CompanyForm, RoleTypeForm, EmployeeForm, RoleLogForm
from django.contrib.auth import login, authenticate
from django.urls import reverse_lazy
from django.views import generic
from django.contrib import messages
from .models import Company, Profile, Role_Type, Employee, Role_Log
from .script import get_employee_roles
from django.shortcuts import render_to_response
from django.views.generic import View
from django.http import JsonResponse

from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User

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

def employee_detail(request, pk):
    employee = Employee.objects.select_related().get(pk=pk)
    roles = get_employee_roles(employee)
    if request.method == 'POST':
        form = RoleLogForm(request.POST)
        if form.is_valid():
            role_log = form.save(commit = False)
            role_log.employee = employee
            role_log.company = employee.company
            role_log.save()
            return redirect( 'employee_detail', pk=employee.pk)


    else: 
        form = RoleLogForm()

    return render(request, 'employee_detail.html', {'form': form, 'roles': roles, 'employee': employee})


def role_log_delete(request, pk):
    role = Role_Log.objects.get(id=pk)
    employee = role.employee
    Role_Log.objects.get(id=pk).delete()
    return redirect('employee_detail', pk=employee.pk)

def employee_edit(request, pk):
    employee = Employee.objects.get(pk=pk)
    if request.method == "POST":
        form = EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            employee = form.save()
            return redirect('employee_detail', pk=employee.pk)
    else:
        form = EmployeeForm(instance=employee)
    return render(request, 'create_employee.html', {"form": form})

class Home_View(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'chart.html', {})

def get_data(request, *args, **kwargs):
    data = {
        'sales': 200,
        'customers': 10
    }
    return JsonResponse(data)


class ChartData(APIView):

    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        data = {

        }
        return Response(data)
