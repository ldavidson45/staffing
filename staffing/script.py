from .models import Role_Log, Employee, Role_Type

#Return all of the roles the user has:

def get_employee_roles(employee):
    roles = Role_Log.objects.all().filter(employee=employee).order_by('-start_date')
    return roles

def get_current_role(employee):
    current_role = Role_Log.objects.get(end_date__isnull=True)
    return current_role