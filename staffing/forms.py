from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser, Profile, Company, Role_Type

class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = CustomUser
        fields = ('username', 'email')

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
        fields = ('title')
