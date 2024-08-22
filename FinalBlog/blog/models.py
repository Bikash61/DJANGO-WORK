from django.db import models

# Create your models here.
class Post(models.Model):
    name = models.CharField(max_length=255)
    content = models.TextField()
    author = models.CharField(max_length=255)
    date = models.DateTimeField(auto_created=True)

    def __str__(self):
        return self.name
    
