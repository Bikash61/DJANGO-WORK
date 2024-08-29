from django.urls import path
from . import views

urlpatterns = [
    path("students/",views.StudentListCreateView.as_view(), name = 'student-list-create' ),
    path("students/<int:pk>/", views.StudentRetrieveUpdateDestroyView.as_view(), name = 'student-retrieve-update-destroy' ),
]