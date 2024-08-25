from django.shortcuts import render
from .models import Job, Internship

# Create your views here.
def index(request):
    return render(request , 'index.html')

def login(request):
    return render(request, 'log-in.html')

def signup(request):
    return render(request, 'sign-up.html')

def home(request):
    return render(request, 'index.html', {'post' : Job.objects.all()})


def joblist(request):
    return render(request, 'joblist.html', {"post": Job.objects.all()})

def postdetail(request):
    return render(request, 'postdetail.html', {'post': Job.objects.all()})

def internship(request):
    return render(request, 'internshiplist.html', {"internship": Internship.objects.all()})