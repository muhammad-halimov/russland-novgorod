# Generated by Django 4.2.9 on 2024-03-23 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='uploadedphotos',
            name='brightness',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AddField(
            model_name='uploadedphotos',
            name='contrast',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AddField(
            model_name='uploadedphotos',
            name='rotation',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='albums',
            name='photo',
            field=models.ImageField(default='ava1.jpg', null=True, upload_to='covers'),
        ),
        migrations.AlterField(
            model_name='uploadedvideos',
            name='cover',
            field=models.ImageField(default='favicon.png', null=True, upload_to='videos/covers'),
        ),
        migrations.AlterField(
            model_name='user',
            name='avatar',
            field=models.ImageField(blank=True, default='avatar.svg', null=True, upload_to='avatars'),
        ),
    ]