from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views
from django.conf.urls import url
from rest_framework import routers

# router = routers.DefaultRouter()
# router.register("roles", views.ChartTest)

urlpatterns = [
    path('signup/', views.sign_up, name='signup'),
    path('profile/<int:pk>/company', views.create_company, name="company_create"),
    path('company/', views.company_detail, name='company_detail'),
    path('employees/', views.employee_list, name="employee_list"),
    path('login/', auth_views.LoginView.as_view(template_name='login_page.html')),
    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html')),
    path('employee/new', views.create_employee, name="create_employee"),
    path('employee/<int:pk>/', views.employee_detail, name="employee_detail"),
    path('role-log/<int:pk>/delete', views.role_log_delete, name='role_log_delete'),
    path('employee/<int:pk>/edit', views.employee_edit, name='employee_edit'),
    url(r'^$', views.Home_View.as_view(), name='home'),
    url('^api/data/<int:pk>', views.get_data, name='api-data'),
    url('api/chart/data/', views.ChartData.as_view()),
]