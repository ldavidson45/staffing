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