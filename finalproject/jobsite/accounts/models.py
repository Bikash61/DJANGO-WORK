from django.contrib.auth.models import User
from django.db import models

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # Additional fields if needed, e.g., profile picture, bio, etc.

    def __str__(self):
        return self.user.username
