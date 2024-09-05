from django.db import models

# Create your models here.
class PageVisit(models.Model):
    #db -> Table 
    path = models.TextField() #col
    timestamp = models.DateTimeField(auto_now_add=True) #col
