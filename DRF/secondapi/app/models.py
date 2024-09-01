from django.db import models

# Create your models here.
class Teacher(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, unique=True)
    phone_number = models.CharField(max_length=20)
    grade = models.CharField(max_length=200)
    teacher_id = models.AutoField(primary_key=True)

    def __str__(self):
        return self.name
    