# Generated by Django 5.1 on 2024-08-25 08:34

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='image',
            field=models.ImageField(default=datetime.datetime(2024, 8, 25, 8, 34, 59, 403110, tzinfo=datetime.timezone.utc), upload_to=''),
            preserve_default=False,
        ),
    ]
