from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('signup/', views.sign_up, name='signup'),
    path('profile/<int:pk>/company', views.create_company, name="company_create"),
    path('company/<int:pk>', views.company_detail, name='company_detail'),
    path('', views.employee_list, name="employee_list"),
    path('login/', auth_views.LoginView.as_view(template_name='login_page.html')),
    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html')),
    path('employee/new', views.create_employee, name="create_employee"),
    path('role-log/<int:pk>', views.edit_role_log, name="edit_role_log")
]

