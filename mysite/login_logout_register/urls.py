from django.urls import path
from login_logout_register.views import *

urlpatterns = [
    path('', login.view, name='login'),
]
