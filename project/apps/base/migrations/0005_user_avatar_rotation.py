# Generated by Django 4.2.9 on 2024-03-23 16:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_user_avatar_brightness_user_avatar_contrast'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='avatar_rotation',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
    ]