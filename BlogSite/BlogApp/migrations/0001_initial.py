# Generated by Django 5.0.3 on 2024-08-13 11:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('slug', models.SlugField(blank=True, unique=True)),
                ('image', models.ImageField(upload_to='blog_images/')),
                ('content', models.TextField()),
                ('excerpt', models.TextField(blank=True, max_length=300)),
                ('published_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]