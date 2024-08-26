from django.shortcuts import render, get_object_or_404, redirect, reverse
from .models import Job, Internship
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    return render(request , 'index.html', {'post' : Job.objects.all(), "internship": Internship.objects.all()})

def login(request):
    return render(request, 'login.html')

def signup(request):
    return render(request, 'signup.html')

def home(request):
    return render(request, 'index.html', {'post' : Job.objects.all(), "internship": Internship.objects.all()})

def joblist(request):
    return render(request, 'joblist.html', {"post": Job.objects.all()})

def postdetail(request):
    return render(request, 'postdetail.html', {'post': Job.objects.all()})

def internship(request):
    return render(request, 'internshiplist.html', {"internship": Internship.objects.all()})

    
def profile(request, post_id =1):
    user = get_object_or_404(User, id=post_id)
    return render(request, 'profile.html', {"user": user})

 
# # Views
# @login_required
# def home(request):
#     return render(request, "index.html", {})
 
def register(request):
    form = UserCreationForm()
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect("home")
        else:
            messages.error(request, "An error occour  during registration")