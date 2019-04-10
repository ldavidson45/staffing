import datetime

from django import forms
from .models import CustomUser, Profile, Company, Role_Type, Employee, Role_Log
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from tempus_dominus.widgets import DatePicker
from django.forms import formset_factory



class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = CustomUser
        fields = ("first_name", "last_name", 'username', 'email', )

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = UserChangeForm.Meta.fields

class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = ('name',)

class RoleTypeForm(forms.ModelForm):
    class Meta:
        model = Role_Type
        fields = ('title',)

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ('name', 'role', 'status')

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

RoleLogFormset = formset_factory(RoleLogForm)
