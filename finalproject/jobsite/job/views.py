from django.shortcuts import render
from .models import Job

# Create your views here.
def index(request):
    return render(request , 'base.html')

def login(request):
    return render(request, 'log-in.html')

def signup(request):
    return render(request, 'sign-up.html')


# Create your views here.
def home(request):
    return render(request, 'index.html', {'post' : Job.objects.all()})

def post_detail(request):
    return render(request, 'article.html', {"post": Job.objects.all()})