from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('add-mine/', views.add_mine, name='add_mine'),
    path('add-tree/', views.add_tree, name='add_tree'),
]
