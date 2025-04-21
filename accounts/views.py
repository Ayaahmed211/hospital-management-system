from django.shortcuts import render, redirect
from django.contrib import messages
from .models import CustomUser
from django.contrib.auth import authenticate, login

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        role = request.POST['role']  # You can store or process roles too!

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, f'Welcome, {user.username}!')
        
            return redirect('/')  # Redirect to dashboard later!
        else:
            messages.error(request, 'Invalid credentials.')
    return render(request, 'accounts/login.html')

def register_patient(request):
    if request.method == 'POST':
        full_name = request.POST['full_name']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 != password2:
            messages.error(request, 'Passwords do not match!')
        else:
            user = CustomUser.objects.create_user(username=email, email=email, password=password1, user_type='patient')
            user.first_name = full_name
            user.save()
            messages.success(request, 'Patient account created successfully!')
            return redirect('login')

    return render(request, 'accounts/register_patient.html')

def register_doctor(request):
    if request.method == 'POST':
        full_name = request.POST['full_name']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 != password2:
            messages.error(request, 'Passwords do not match!')
        else:
            user = CustomUser.objects.create_user(username=email, email=email, password=password1, user_type='doctor')
            user.first_name = full_name
            user.save()
            messages.success(request, 'Doctor account created successfully!')
            return redirect('login')

    return render(request, 'accounts/register_doctor.html')

def register_admin(request):
    if request.method == 'POST':
        full_name = request.POST['full_name']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        verification_code = request.POST['verification_code']

        if verification_code != "ADMIN123":  # You can secure this via settings later!
            messages.error(request, 'Invalid verification code!')
        elif password1 != password2:
            messages.error(request, 'Passwords do not match!')
        else:
            user = CustomUser.objects.create_user(username=email, email=email, password=password1, user_type='admin')
            user.first_name = full_name
            user.is_staff = True  # Mark admin users
            user.save()
            messages.success(request, 'Admin account created successfully!')
            return redirect('login')

    return render(request, 'accounts/register_admin.html')
