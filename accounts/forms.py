from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser, PatientProfile, DoctorProfile, AdminProfile

class CustomUserForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password1', 'password2', 'user_type']

# Patient Registration Form
class PatientProfileForm(forms.ModelForm):
    class Meta:
        model = PatientProfile
        fields = [
            'date_of_birth', 'gender', 'phone_number', 'address',
            'emergency_contact', 'insurance_details', 'medical_history'
        ]

# Doctor Registration Form
class DoctorProfileForm(forms.ModelForm):
    class Meta:
        model = DoctorProfile
        fields = [
            'phone_number', 'department', 'qualification',
            'license_number', 'experience_years', 'certification_document'
        ]

# Admin Registration Form
class AdminProfileForm(forms.ModelForm):
    class Meta:
        model = AdminProfile
        fields = ['phone_number', 'verification_code']
