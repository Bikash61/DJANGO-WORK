from django.db import models

# Create your models here.
class Student(models.Model):
    name=models.CharField(max_length=50)
    age=models.IntegerField()
    address=models.CharField(max_length=50)
    pic=models.ImageField(upload_to='media/')
    
    def __str__(self):
        return self.name