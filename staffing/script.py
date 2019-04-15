from .models import Role_Log, Employee, Role_Type, Profile
from django.http import JsonResponse
from django.db.models import Count, Sum
import datetime
from django.db.models.functions import TruncMonth
from django.utils.dateparse import parse_date
import calendar


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
    today = datetime.date.today()
    beginning_of_month = today.replace(day=1)
    month_year_list = []
    i = 0
    while i < 365:
        date = beginning_of_month - datetime.timedelta(i)
        month_year_list.append(date)
        next_month = date - datetime.timedelta(1)
        i += calendar.monthrange(next_month.year, next_month.month)[1]

    return list(reversed(month_year_list))

def get_roles_count():
    # user_profile = Profile.objects.filter(user=user)
    # company = user_profile.company
    roles = Role_Type.objects.all()
    dates = get_months()
    month_datasets = []
    today = datetime.datetime.today()
    colors =['#ff513e', '#3eff8b', '#653eff', '#ffb23e', '#3eb2ff', '#9936fd', '#ff1bff','#ff513e','#3eff8b','#653eff', '#ffb23e']
    i = 0
    for role in roles:
        data_dict={}
        data_dict['label'] = role.title
        data_dict['data'] = []
        data_dict['backgroundColor'] = colors[i]
        i += 1
        filtered_logs = Role_Log.objects.filter(role_type= role)
        for month in dates:
            month_count=0
            for log in filtered_logs:
                if log.end_date is None:
                    end = datetime.datetime(today.year, today.month, today.day)
                    start = datetime.datetime(log.start_date.year, log.start_date.month, log.start_date.day)
                    month = datetime.datetime(month.year, month.month, month.day)
                    if end > month and month > start: month_count += 1
                else:
                    end = datetime.datetime(log.end_date.year, log.end_date.month, log.end_date.day)
                    start = datetime.datetime(log.start_date.year, log.start_date.month, log.start_date.day)
                    month = datetime.datetime(month.year, month.month, month.day)
                    if end > month and month > start: month_count += 1
            data_dict['data'].append(month_count)
        month_datasets.append(data_dict)
    return month_datasets