from django.shortcuts import render
from .models import StudentDetail

# Create your views here.
def home(req):
    studentsdata= StudentDetail.objects.all()
    return render(req, 'Home/home.html', {'students': studentsdata})