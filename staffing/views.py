from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm, CompanyForm, RoleTypeForm
from django.contrib.auth import login, authenticate
from django.urls import reverse_lazy
from django.views import generic
from .models import Company, Profile, Role_Type, Employee
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
    if request.method == 'POST':
        form = CompanyForm(request.POST)
        if form.is_valid():
            company = form.save()
            Profile.objects.filter(pk=pk).update(company=company)
            return redirect('/')
    else:
        form = CompanyForm()
    return render(request, 'create_company.html', {'form': form})

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

    