from django.db import models

# Create your models here.

class Problem(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    Images = models.ImageField()
    description = models.TextField()
    difficulty = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Solution(models.Model):
    id = models.AutoField(primary_key = True)
    name = models.CharField(max_length =255)
    description = models.TextField()


    def __str__(self):
        return self.name

class About(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name