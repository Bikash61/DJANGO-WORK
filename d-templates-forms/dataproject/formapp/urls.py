from django.urls import path
from .views import Student

urlpatterns = [
    path('', Student, name ='home')
    
]
