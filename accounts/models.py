from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    USER_TYPE_CHOICES = (
        ('patient', 'Patient'),
        ('doctor', 'Doctor'),
        ('admin', 'Admin'),

    )
    user_type = models.CharField(max_length=20, choices=USER_TYPE_CHOICES, default='patient')

    # Adding related_name to avoid the clash with default User model
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='customuser_set',  # Custom related name
        blank=True
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='customuser_permissions',  # Custom related name
        blank=True
    )

class PatientProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=10)
    phone_number = models.CharField(max_length=20)
    address = models.TextField()
    emergency_contact = models.CharField(max_length=20)
    insurance_details = models.CharField(max_length=255, blank=True, null=True)
    medical_history = models.TextField(blank=True, null=True)


class DoctorProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=20)
    department = models.CharField(max_length=50)
    qualification = models.CharField(max_length=100)
    license_number = models.CharField(max_length=50)
    experience_years = models.PositiveIntegerField()
    certification_document = models.FileField(upload_to='certifications/')


class AdminProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=20)
    verification_code = models.CharField(max_length=20)
from django.db import models

# Create your models here.
