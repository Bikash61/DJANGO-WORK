from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from taggit.managers import TaggableManager
from django.urls import reverse
from django.core.exceptions import ValidationError
from ckeditor_uploader.fields import RichTextUploadingField
from django.utils.deconstruct import deconstructible

class Category(models.TextChoices):
    SALES = 'sales'
    MARKETING = 'marketing'
    BUSINESS = 'business'
    POLITICS = 'politics'
    ART = 'art'

class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager, self).get_queryset().filter(status='published')

@deconstructible
class ImageSizeValidator:
    def __init__(self, max_size_mb=0.5):
        self.max_size_mb = max_size_mb

    def __call__(self, fieldfile_obj):
        filesize = fieldfile_obj.file.size
        megabyte_limit = self.max_size_mb
        if filesize > megabyte_limit * 1024 * 1024:
            raise ValidationError(
                f"File size exceeds the maximum limit of {megabyte_limit}MB."
            )

class Post(models.Model):
    title = models.CharField(max_length=200, help_text="Blog post title")
    slug = models.SlugField(max_length=600, unique_for_date='publish')
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='blog_post', help_text="Choose author for the post")
    category = models.CharField(
        max_length=50, choices=Category.choices, default=Category.SALES,
        help_text="Category for the post"
    )
    image = models.ImageField(
        upload_to='images/',
        null=True,
        validators=[ImageSizeValidator(max_size_mb=0.5)],
        help_text="Image should be less than 500MB"
    )
    readTime = models.IntegerField(
        null=True, help_text="Read time for the post")
    body = RichTextUploadingField(help_text="Your blog post")
    featured = models.BooleanField(
        default=False, help_text="Check to make the post featured")
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    STATUS_CHOICES = (('draft', 'Draft'), ('published', 'Published'))
    status = models.CharField(
        max_length=20, choices=STATUS_CHOICES, default='draft'
    )
    objects = models.Manager()
    published = PublishedManager()

    # tags = TaggableManager()

    class Meta:
        ordering = ('-publish',)

    def save(self, *args, **kwargs):
        if self.featured:
            try:
                temp = Post.objects.get(featured=True)
                if self != temp:
                    temp.featured = False
                    temp.save()
            except Post.DoesNotExist:
                pass
        super(Post, self).save(*args, **kwargs)

    def __str__(self):
        return self.title