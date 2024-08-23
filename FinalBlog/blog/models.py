# from django.db import models
# from django.contrib.auth.models import AbstractUser

# # Custom User model with limited permissions
# class User(AbstractUser):
#     pass  # Use this model for local user authentication

# # Category model
# class Category(models.Model):
#     name = models.CharField(max_length=100)
#     description = models.TextField()

#     def __str__(self):
#         return self.name

# # Comment model
# class Comment(models.Model):
#     text = models.TextField()
#     user = models.ForeignKey(User, on_delete=models.CASCADE)  # Link to custom user
#     post = models.ForeignKey('Post', related_name='comments', on_delete=models.CASCADE)

#     def __str__(self):
#         return self.text

# # Author model
# class Author(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     name = models.CharField(max_length=100)
#     surname = models.CharField(max_length=100)
#     email = models.EmailField(max_length=100)

#     def __str__(self):
#         return f'{self.name} {self.surname}'

# # Post model
# class Post(models.Model):
#     title = models.CharField(max_length=255)
#     content = models.TextField()
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
#     category = models.ForeignKey(Category, on_delete=models.CASCADE)
#     author = models.ForeignKey(Author, on_delete=models.CASCADE)
    
#     def __str__(self):
#         return self.title

#     def can_be_updated_by(self, user):
#         return self.author.user == user
