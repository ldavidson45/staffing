from django.shortcuts import render
from .forms import CustomUserCreationForm
from django.urls import reverse_lazy
from django.views import generic
# Create your views here.

class SignUp(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('signup')
    template_name = 'signup.html'