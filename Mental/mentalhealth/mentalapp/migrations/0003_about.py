# Generated by Django 5.1 on 2024-08-14 11:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mentalapp', '0002_solution'),
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
            ],
        ),
    ]
