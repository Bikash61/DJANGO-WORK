from django.shortcuts import render
from .models import *

# Create your views here.
def home(request):
    problem = Problem.objects.all()
    return render(request, 'home.html', {"problems":problem})

def about(request):
    about = About.objects.all()
    return render(request, 'about.html', {'abouts':about})

