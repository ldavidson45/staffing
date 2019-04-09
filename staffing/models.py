from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.

class Company(models.Model):
    name= models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = 'companies'
        verbose_name = 'company name'

    def __str__(self):
        return self.name

class CustomUserManager(UserManager):
    pass

class CustomUser(AbstractUser):
    objects = CustomUserManager()

class Profile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, related_name='users', on_delete=models.CASCADE, blank=True,
    null=True,)

    class Meta: 
        verbose_name_plural = 'profiles'
        verbose_name = 'profile'

    def __str__(self):
        return self.user.username

class Role_Type(models.Model):
    title=models.CharField(max_length=50)
    company=models.ForeignKey(Company, on_delete=models.CASCADE, related_name='roles')
    class Meta:
        verbose_name_plural = "role types"
        verbose_name="role type"
    def __str__(self):
        return self.title

class Employee(models.Model):
    status_choices = (
    ('active', 'active'),
    ('inactive', 'inactive')
)
    name=models.CharField(max_length=200)
    company=models.ForeignKey(Company, on_delete=models.CASCADE, related_name='employees')
    role=models.ForeignKey(Role_Type, on_delete=models.CASCADE, related_name='employees')
    status= models.CharField(max_length=2,
        choices=status_choices,
        default='active')
    class Meta:
        verbose_name_plural = "employees"
        verbose_name='employee'
    def __str__(self):
        return self.name