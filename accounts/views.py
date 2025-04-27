from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.db import transaction
from .models import CustomUser, PatientProfile, DoctorProfile, AdminProfile
from .forms import PatientProfileForm, DoctorProfileForm, AdminProfileForm, CustomUserForm
from django.contrib.auth.decorators import login_required
from django.core.files.storage import FileSystemStorage

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
def register(request):
    if request.method == 'POST':
        user_form = CustomUserForm(request.POST)
        
        user_type = request.POST.get('user_type')
        
        try:
            with transaction.atomic():
                if user_form.is_valid():
                    user = user_form.save(commit=False)
                    user.set_password(user_form.cleaned_data['password1'])
                    user.user_type = user_type
                    user.save()
                    
                    if user_type == 'patient':
                        PatientProfile.objects.create(
                            user=user,
                            date_of_birth=request.POST.get('date_of_birth'),
                            gender=request.POST.get('gender'),
                            phone_number=request.POST.get('phone_number'),
                            address=request.POST.get('address'),
                            emergency_contact=request.POST.get('emergency_contact'),
                            insurance_details=request.POST.get('insurance_details'),
                            medical_history=request.POST.get('medical_history')
                        )
                    elif user_type == 'doctor':
                        certification_file = request.FILES.get('certification_document')
                        if certification_file:
                            fs = FileSystemStorage()
                            filename = fs.save(f'certifications/{certification_file.name}', certification_file)
                        
                        DoctorProfile.objects.create(
                            user=user,
                            phone_number=request.POST.get('phone_number'),
                            department=request.POST.get('department'),
                            qualification=request.POST.get('qualification'),
                            license_number=request.POST.get('license_number'),
                            experience_years=request.POST.get('experience_years'),
                            certification_document=filename if certification_file else None
                        )
                    elif user_type == 'admin':
                        AdminProfile.objects.create(
                            user=user,
                            phone_number=request.POST.get('phone_number'),
                            verification_code=request.POST.get('verification_code')
                        )
                    
                    messages.success(request, 'Registration successful! Please log in.')
                    return redirect('login')
                
                for field, errors in user_form.errors.items():
                    for error in errors:
                        messages.error(request, f"{field}: {error}")
        
        except Exception as e:
            messages.error(request, f"An error occurred during registration: {str(e)}")
            return redirect('register')
    
    else:
        user_form = CustomUserForm()
    
    return render(request, 'accounts/register.html', {
        'user_form': user_form
    })

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