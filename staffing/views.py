from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm, CompanyForm, RoleTypeForm, EmployeeForm, RoleLogForm
from django.contrib.auth import login, authenticate
from .models import Company, Profile, Role_Type, Employee, Role_Log, CustomUser, Profile
from .script import get_employee_roles, get_roles_count, get_months_str
from django.views.generic import View
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Company, Profile, Role_Type, Employee, Role_Log
from .script import get_employee_roles
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated

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

@login_required
def create_company(request, pk):
    user = request.user
    if request.method == 'POST':
        form = CompanyForm(request.POST)
        if form.is_valid():
            company = form.save()
            Profile.objects.filter(pk=pk).update(company=company)
            return redirect('/company/')
    else:
        form = CompanyForm()
    return render(request, 'create_company.html', {'form': form, 'user':user})

@login_required
def company_detail(request):
    user = request.user
    company = user.profile.company
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

@login_required
def employee_list(request):
    pk = request.user.profile.company.pk
    company = Company.objects.get(pk=pk)
    active_employees = Employee.objects.all().filter(company=company,status='active')
    inactive_employees = Employee.objects.all().filter(company=company,status='inactive')


    return render(request, 'employee_list.html', {'active': active_employees, 'inactive': inactive_employees})

@login_required
def create_employee(request):
    pk = request.user.profile.company.pk
    company = Company.objects.get(pk=pk)
    if request.method == 'POST':
        form = EmployeeForm(company, request.POST)
        if form.is_valid():
            employee = form.save(commit = False)
            employee.company = company
            employee.save()
            return redirect('employee_list')
    else:
        form = EmployeeForm(company)
    return render(request, 'create_employee.html', {'form': form})

@login_required
def employee_detail(request, pk):
    employee = Employee.objects.select_related().get(pk=pk)
    roles = get_employee_roles(employee)
    company = request.user.profile.company
    if request.method == 'POST':
        form = RoleLogForm(company, request.POST)
        if form.is_valid():
            role_log = form.save(commit = False)
            role_log.employee = employee
            role_log.company = employee.company
            role_log.save()
            return redirect( 'employee_detail', pk=employee.pk)
    else: 
        form = RoleLogForm(company)

    return render(request, 'employee_detail.html', {'form': form, 'roles': roles, 'employee': employee})

@login_required
def role_log_delete(request, pk):
    role = Role_Log.objects.get(id=pk)
    employee = role.employee
    Role_Log.objects.get(id=pk).delete()
    return redirect('employee_detail', pk=employee.pk)

@login_required
def employee_edit(request, pk):
    employee = Employee.objects.get(pk=pk)
    company = request.user.profile.company
    if request.method == "POST":
        form = EmployeeForm(company, request.POST, instance=employee)
        if form.is_valid():
            employee = form.save()
            return redirect('employee_detail', pk=employee.pk)
    else:
        form = EmployeeForm(company, instance=employee)
    return render(request, 'create_employee.html', {"form": form})

class Home_View(LoginRequiredMixin, View):
    login_url = '/login/'
    redirect_field_name = 'redirect_to'
    def get(self, request, *args, **kwargs):
        return render(request, 'chart.html', {})



class ChartData(APIView):
    authentication_classes = (SessionAuthentication, BasicAuthentication)
    permission_classes = (IsAuthenticated,)
    def get(self, request, format=None):
        user = self.request.user
        datasets = get_roles_count(user)
        labels = get_months_str()
        default = []
        data = {
            "labels": labels,
            "datasets": datasets

        }
        return Response(data)
