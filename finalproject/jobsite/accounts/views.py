from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages

def signup_view(request):
    if request.method == 'POST':
        email = request.POST['email']
        name = request.POST['name']
        password = request.POST['password']
        user = User.objects.create_user(username=name, email=email, password=password)
        messages.success(request, "Signup successful! You can now log in.")
        return redirect('login')
    return render(request, 'accounts/signup.html')

def login_view(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, username=User.objects.get(email=email).username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')  # Redirect to blog list or any other page
        else:
            messages.error(request, "Invalid credentials")
    return render(request, 'accounts/login.html')

def logout_view(request):
    logout(request)
    return redirect('login')
