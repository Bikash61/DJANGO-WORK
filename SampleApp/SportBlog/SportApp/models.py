from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=255)
    age = models.IntegerField()
    email = models.EmailField(max_length=255, unique=True)
    phone_number = models.IntegerField()


    def __str__(self):
        return self.name