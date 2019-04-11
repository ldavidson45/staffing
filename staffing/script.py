from .models import Role_Log, Employee, Role_Type

#Return all of the roles the user has:

def get_employee_roles(employee):
    roles = Role_Log.objects.all().filter(employee=employee).order_by('-start_date')
    return roles

def get_active_employees(company):
    active_employees = Employee.objects.filter(company=company, status='active').count()

    return active_employees
    
