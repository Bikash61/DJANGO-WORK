from django.urls import path
from . import views

urlpatterns = [
    path('teacher/', views.TeacherListCreateView.as_view(), name='student-list-create'),
    path('teacher/<int:pk>/', views.TeacherRetrieveUpdateDestroyView.as_view(), name='teacher-retrieve-update-destroy')

]
