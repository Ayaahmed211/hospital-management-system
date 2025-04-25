# accounts/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('register/patient/', views.register_patient, name='register_patient'),
    path('register/doctor/', views.register_doctor, name='register_doctor'),
    path('register/admin/', views.register_admin, name='register_admin'),
    path('profile/patient/', views.patient_profile, name='patient_profile'),
    path('profile/doctor/', views.doctor_profile, name='doctor_profile'),
    path('profile/admin/', views.admin_profile, name='admin_profile'),
]
