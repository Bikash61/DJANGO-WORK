from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField(max_length=100)
    grade = models.IntegerField()
    school = models.CharField(max_length=100)

    def __str__(self):
        self.name