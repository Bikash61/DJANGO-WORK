from django.shortcuts import render
from .models import Job

# Create your views here.
def index(request):
    return render(request , 'index.html')

def login(request):
    return render(request, 'log-in.html')

def signup(request):
    return render(request, 'sign-up.html')

def home(request):
    return render(request, 'index.html', {'post' : Job.objects.all()})

def post_detail(request):
    return render(request, 'article.html', {"post": Job.objects.all()})