# Generated by Django 4.2.9 on 2024-03-24 12:02

import base.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0011_alter_uploadedphotos_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='uploadedphotos',
            name='reducted',
            field=models.ImageField(default='ava1.jpg', null=True, upload_to=base.models.get_photo_reducted_upload_path),
        ),
    ]
