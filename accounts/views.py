from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.db import transaction
from .models import CustomUser, PatientProfile, DoctorProfile, AdminProfile
from .forms import PatientProfileForm, DoctorProfileForm, AdminProfileForm
from django.contrib.auth.decorators import login_required

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            messages.success(request, f'Welcome, {user.username}!')
            if user.user_type == 'patient':
                return redirect('patient_profile')
            elif user.user_type == 'doctor':
                return redirect('doctor_profile')
            elif user.user_type == 'admin':
                return redirect('admin_profile')
            else:
                return redirect('/')
        else:
            messages.error(request, 'Invalid credentials.')
    return render(request, 'accounts/login.html')

@transaction.atomic
def register_patient(request):
    if request.method == 'POST':
        full_name = request.POST.get('full_name', '')
        email = request.POST.get('email', '')
        password1 = request.POST.get('password1', '')
        password2 = request.POST.get('password2', '')
        dob = request.POST.get('date_of_birth', '')
        gender = request.POST.get('gender', '')
        phone = request.POST.get('phone_number', '')
        address = request.POST.get('address', '')
        emergency = request.POST.get('emergency_contact', '')
        insurance = request.POST.get('insurance_details', '')
        history = request.POST.get('medical_history', '')

        if password1 != password2:
            messages.error(request, 'Passwords do not match!')
        elif not all([full_name, email, dob, gender, phone, address, emergency]):
            messages.error(request, 'Please fill in all required fields.')
        else:
            user = CustomUser.objects.create_user(
                username=email,
                email=email,
                password=password1,
                first_name=full_name,
                user_type='patient'
            )
            PatientProfile.objects.create(
                user=user,
                date_of_birth=dob,
                gender=gender,
                phone_number=phone,
                address=address,
                emergency_contact=emergency,
                insurance_details=insurance,
                medical_history=history
            )
            messages.success(request, 'Patient account created successfully!')
            return redirect('login')

    return render(request, 'accounts/register_patient.html')

@transaction.atomic
def register_doctor(request):
    if request.method == 'POST':
        full_name = request.POST['full_name']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        phone = request.POST['phone_number']
        department = request.POST['department']
        qualification = request.POST['qualification']
        license_num = request.POST['license_number']
        experience = request.POST['experience_years']
        cert_doc = request.FILES.get('certification_document')

        if password1 != password2:
            messages.error(request, 'Passwords do not match!')
        else:
            user = CustomUser.objects.create_user(
                username=email,
                email=email,
                password=password1,
                first_name=full_name,
                user_type='doctor'
            )
            DoctorProfile.objects.create(
                user=user,
                phone_number=phone,
                department=department,
                qualification=qualification,
                license_number=license_num,
                experience_years=experience,
                certification_document=cert_doc
            )
            messages.success(request, 'Doctor account created successfully!')
            return redirect('login')
    return render(request, 'accounts/register_doctor.html')

@transaction.atomic
def register_admin(request):
    if request.method == 'POST':
        full_name = request.POST['full_name']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        phone = request.POST['phone_number']
        verification_code = request.POST['verification_code']

        if verification_code != "ADMIN123":
            messages.error(request, 'Invalid verification code!')
        elif password1 != password2:
            messages.error(request, 'Passwords do not match!')
        else:
            user = CustomUser.objects.create_user(
                username=email,
                email=email,
                password=password1,
                first_name=full_name,
                user_type='admin',
                is_staff=True
            )
            AdminProfile.objects.create(
                user=user,
                phone_number=phone,
                verification_code=verification_code
            )
            messages.success(request, 'Admin account created successfully!')
            return redirect('login')
    return render(request, 'accounts/register_admin.html')

@login_required
def patient_profile(request):
    profile, created = PatientProfile.objects.get_or_create(user=request.user)

    if request.method == 'POST':
        form = PatientProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully!')
    else:
        form = PatientProfileForm(instance=profile)

    return render(request, 'accounts/patient_profile.html', {'form': form})

@login_required
def doctor_profile(request):
    profile, created = DoctorProfile.objects.get_or_create(user=request.user)

    if request.method == 'POST':
        form = DoctorProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully!')
    else:
        form = DoctorProfileForm(instance=profile)

    return render(request, 'accounts/doctor_profile.html', {'form': form})

@login_required
def admin_profile(request):
    profile, created = AdminProfile.objects.get_or_create(user=request.user)

    if request.method == 'POST':
        form = AdminProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully!')
    else:
        form = AdminProfileForm(instance=profile)

    return render(request, 'accounts/admin_profile.html', {'form': form})