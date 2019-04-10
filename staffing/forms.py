from django import forms
from .models import CustomUser, Profile, Company, Role_Type, Employee, Role_Log
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.forms import widgets

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
    start_date = forms.DateTimeField(input_formats=['%d/%m/%Y %H:%M'])
    end_date = forms.DateTimeField(input_formats=['%d/%m/%Y %H:%M'])

    class Meta:
        model = Role_Log
        widgets = {'start_date': forms.DateInput(attrs={'class': 'datepicker'})}
        fields = ('role_type', 'start_date', 'end_date')

