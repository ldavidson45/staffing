from .models import Role_Log, Employee, Role_Type
from django.http import JsonResponse
from django.db.models import Count
import datetime
from django.db.models.functions import TruncMonth
from calendar import monthrange

from collections import OrderedDict
#Return all of the roles the user has:

def get_employee_roles(employee):
    roles = Role_Log.objects.all().filter(employee=employee).order_by('-start_date')
    return roles

def get_roles_count():
    roles = Role_Type.objects.all()
    test_months = Role_Log.objects.annotate(month=TruncMonth('start_date')).values('month').order_by('month')
    test = {}
    dict = {}


    for role in roles:
        count = Role_Log.objects.filter(role_type=role).count()
        items = Role_Log.objects.filter(role_type=role)
        test["label"] = role.title
        dict[role.title] = count

        return dict

def get_list_of_months():
    i = 0
    today = datetime.datetime.today()
    month_year_list = []
    while i < 365:
        date = today - datetime.timedelta(i)
        month_year_list.append(date.strftime('%b %Y'))
        i += 30
    print(today.strftime("%b %Y"))
    return reversed(month_year_list)


# {
#             labels: labels,
#             datasets: [{
#                 label: "# of Votes",
#                 data: defaultdata,
#                 backgroundColor: '#D6E9C6' // green

#               },
#                { label: "Dataset2",
#                data: defaultdata,
#                backgroundColor: '#FAEBCC' // yellow

#               }
#               ]
#             },
# Role_Log.objects.filter(start_date__year__gte=year,
#                               start_date__month__gte=month,
#                               end_date__year__lte=year,
#                               end_date__month__lte=month, role_type=role)