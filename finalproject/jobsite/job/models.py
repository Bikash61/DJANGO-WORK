from django.db import models

# Create your models here.
class Job(models.Model):
    title = models.CharField(max_length=255)
    shortdescription = models.TextField()
    description = models.TextField()
    image = models.ImageField()
    location = models.CharField(max_length=255)
    salary = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.title
        
class Internship(models.Model):
    title = models.CharField(max_length=255)
    shortdescription = models.TextField()
    description = models.TextField()
    image = models.ImageField()
    location = models.CharField(max_length=255)
    salary = models.CharField(max_length=255)

    def __str__(self):
        return self.title