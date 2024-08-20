from django.contrib import admin
from .models import *

class CategoryAdmin(admin.ModelAdmin):
    pass

class PostAdmin(admin.ModelAdmin):
    pass

class CommentAdmin(admin.ModelAdmin):
    pass

# Register your models here.
admin.site.register(Post)
admin.site.register(Category)
admin.site.register(Comment)
