# views.py
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .models import Profile

def home(request):
    return render(request, 'home.html')

def mines(request):
    return render(request, 'mines.html')

def bogs(request):
    return render(request, 'bogs.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            error_message = 'Invalid username or password'
            return render(request, 'login.html', {'error_message': error_message})
    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect('home')

def profile(request):
    user = request.user
    profile, created = Profile.objects.get_or_create(user=user)
    return render(request, 'profile.html', {'profile': profile})

def admin_panel(request):
    if request.user.is_staff:
        users = User.objects.all()
        profiles = Profile.objects.all()
        return render(request, 'admin_panel.html', {'users': users, 'profiles': profiles})
    else:
        return redirect('home')



