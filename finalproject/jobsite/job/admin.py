from django.contrib import admin
from .models import Job, Internship

# Register your models here.
@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = ('title', 'shortdescription', 'location', 'created_at')
    
admin.site.register(Internship)
