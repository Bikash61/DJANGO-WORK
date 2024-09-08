# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('mines/', views.mines, name='mines'),
    path('bogs/', views.bogs, name='bogs'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('profile/', views.profile, name='profile'),
    path('admin_panel/', views.admin_panel, name='admin_panel'),
]
