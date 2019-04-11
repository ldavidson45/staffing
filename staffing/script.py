from .models import Role_Log, Employee, Role_Type
from django.http import JsonResponse
from django.db.models import Count, Sum
import datetime
from django.db.models.functions import TruncMonth
from django.utils.dateparse import parse_date

from collections import OrderedDict
#Return all of the roles the user has:

def get_employee_roles(employee):
    roles = Role_Log.objects.all().filter(employee=employee).order_by('-start_date')
    return roles


def get_months_str():
    i = 0
    today = datetime.datetime.today()
    month_year_list = []
    while i < 365:
        date = today - datetime.timedelta(i)
        month_year_list.append(date.strftime('%b %Y'))
        i += 30
    print(today.strftime("%b %Y"))
    return reversed(month_year_list)

def get_months():
    today = datetime.datetime.today()
    month_year_list = []
    i = 0
    while i < 365:
        date = today - datetime.timedelta(i)
        month_year_list.append((date.month, date.year))
        i += 30
    months_descending=reversed(month_year_list)
    return list(reversed(month_year_list))



def get_roles_count():
    roles = Role_Type.objects.all()
    role_logs = Role_Log.objects.all()
    months = get_months()
    month_datasets = []
    colors =['#D6E9C6', '#FAEBCC','#ebccfa', '#20c72b','#20c7bb','#c76320']
    i = 0
    for role in roles:
        data_dict={}
        data_dict['label'] = role.title
        data_dict['data'] = []
        data_dict['backgroundColor'] = colors[i]
        i+= 1
        for month in months:
            count = role_logs.filter(role_type__title= role, start_date__month=month[0], start_date__year=month[1]).count()
            data_dict['data'].append(count)
        month_datasets.append(data_dict)
    print(month_datasets)
    return month_datasets


