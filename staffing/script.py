from .models import Role_Log, Employee, Role_Type
from django.http import JsonResponse
from django.db.models import Count

#Return all of the roles the user has:

def get_employee_roles(employee):
    roles = Role_Log.objects.all().filter(employee=employee).order_by('-start_date')
    return roles

def get_roles():
    roles = Role_Type.objects.all()
    dict = {}
    for role in roles:
        count = Role_Log.objects.filter(role_type=role).count()
        print(count)
        dict[role.title] = count

    return dict

