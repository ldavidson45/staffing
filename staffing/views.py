from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm, CompanyForm
from django.contrib.auth import login, authenticate
from django.urls import reverse_lazy
from django.views import generic
from .models import Company, Profile
# Create your views here.

# class SignUp(generic.CreateView):
#     form_class = CustomUserCreationForm
#     success_url = reverse_lazy('signup')
#     template_name = 'signup.html'


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


    