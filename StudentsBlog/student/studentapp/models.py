from django.db import models

# Create your models here.
class StudentDetail(models.Model):
    name = models.CharField(max_length=100)
    rollno = models.IntegerField()
    age = models.IntegerField()
    class Meta:
        db_table = 'student'
    def __str__(self):
        return self.name    

class TeacherDetail(models.Model):
    name = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)
    age = models.IntegerField()
    class Meta:
        db_table = 'teacher'
    
    def __str__(self):
        return self.name    
