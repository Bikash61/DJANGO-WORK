
from django.urls import path
from .views import *

#urls-

urlpatterns = [
    path('', view_base),
    path('', view_register, name="register"),
    path('', view_login, name="login"),
    path('', view_logout, name="logout_page"),
]