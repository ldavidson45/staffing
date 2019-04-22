import datetime

from django import forms
from .models import CustomUser, Profile, Company, Role_Type, Employee, Role_Log
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from tempus_dominus.widgets import DatePicker
from django.forms import formset_factory



class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = CustomUser
        fields = ("first_name", "last_name", 'username', 'email', 'password1', 'password2' ) 
        widgets = {
            'first_name': forms.TextInput(attrs={'size': 20, 'class': 'form-input'}),
            'last_name': forms.TextInput(attrs={'size': 20, 'class': 'form-input'}),
            'username': forms.TextInput(attrs={'size': 20, 'class': 'form-input'}, ),
            'email': forms.TextInput(attrs={ 'class': 'form-input'}),
        }

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = UserChangeForm.Meta.fields

class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = ('name',)
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Company Name', 'class':'form-input'})
        }

            

class RoleTypeForm(forms.ModelForm):
    class Meta:
        model = Role_Type
        fields = ('title',)

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ('name', 'role', 'status')
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Name', 'class':'form-input'}),
        }
    def __init__(self, company, *args, **kwargs):
        super(EmployeeForm, self).__init__(*args, **kwargs)
        self.fields['role'].queryset = Role_Type.objects.filter(company=company)

class RoleLogForm(forms.ModelForm):
    class Meta:
        model = Role_Log
        fields = ('role_type', 'start_date', 'end_date')
        widgets = {
            'start_date': DatePicker(attrs={
                'append': 'fa fa-calendar',
                'data-target': '#datetimepicker4'}),
            'end_date': DatePicker(attrs={'append': 'fa fa-calendar'})
            }
    def __init__(self, company, *args, **kwargs):
        super(RoleLogForm, self).__init__(*args, **kwargs)
        self.fields['role_type'].queryset = Role_Type.objects.filter(company=company)

