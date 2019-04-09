from django.urls import path

from . import views

urlpatterns = [
    path('signup/', views.sign_up, name='signup'),
    path('profile/<int:pk>/company', views.create_company, name="company_create"),
    path('company/<int:pk>', views.company_detail, name='company_detail')
]