from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class UserDetails(models.Model):
    username = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)



    def __str__(self):
        return self.username
    