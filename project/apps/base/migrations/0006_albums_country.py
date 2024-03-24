# Generated by Django 4.2.9 on 2024-03-23 16:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0005_user_avatar_rotation'),
    ]

    operations = [
        migrations.AddField(
            model_name='albums',
            name='country',
            field=models.CharField(blank=True, choices=[('США', 'Соединенные Штаты Америки'), ('РОССИЯ', 'Российская Федерация'), ('ГЕРМАНИЯ', 'Федеративная РЕСПУБЛИКА Германия'), ('ЯПОНИЯ', 'Королевство Япония'), ('ФРАНЦИЯ', 'Французская Республика')], max_length=256, null=True),
        ),
    ]
