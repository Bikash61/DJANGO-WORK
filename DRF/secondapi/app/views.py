from .models import Student
from .serializers import TeacherSerializers
from rest_framework import generics

class TeacherListCreateView(generics.ListCreateAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializers

class TeacherRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializers
