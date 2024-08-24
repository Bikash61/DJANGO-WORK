from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'base.html')

def login(request):
    return render(request, 'log-in.html')

def signup(request):
    return render(request, 'sign-up.html')

def home(request):
    return render(request, 'index.html')
