from django.db import models
from django.contrib.auth.models import AbstractUser
from uuid import uuid4


class User(AbstractUser):
    username = models.CharField(max_length=256, null=True)
    email = models.EmailField(unique=True, null=True)
    login = models.CharField(max_length=256, null=True)
    avatar = models.ImageField(null=True, blank=True, upload_to='avatars', default="avatar.svg")
    avatar_brightness = models.CharField(max_length=256, null=True, blank=True)
    avatar_contrast = models.CharField(max_length=256, null=True, blank=True)
    avatar_rotation = models.CharField(max_length=256, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    class Meta:
        ordering = ['-id', '-updated']
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def __str__(self):
        return self.username or self.email


class Regions(models.Model):
    name = models.CharField(max_length=256, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-id', '-updated']
        verbose_name = 'Region'
        verbose_name_plural = 'Regions'

    def __str__(self):
        return self.name


class Albums(models.Model):
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    photo = models.ImageField(null=True, upload_to='covers', default="ava1.jpg")
    brightness = models.CharField(max_length=256, null=True, blank=True)
    contrast = models.CharField(max_length=256, null=True, blank=True)
    rotation = models.CharField(max_length=256, null=True, blank=True)
    title = models.CharField(max_length=256, null=True)
    description = models.TextField(null=True, blank=True)
    tags = models.CharField(max_length=256, null=True, blank=True)
    status = models.BooleanField(default=False)
    coauthors = models.ManyToManyField(User, related_name='coauthors', blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-id', '-updated']
        verbose_name = 'Album'
        verbose_name_plural = 'Albums'

    def __str__(self):
        return self.title


def get_photo_upload_path(instance, filename):
    unique_filename = str(uuid4())  # Генерируем случайное уникальное значение
    return f"photos/{unique_filename}_{filename}"  # Путь для сохранения файла с использованием уникального значения


class UploadedPhotos(models.Model):
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    photo = models.ImageField(null=True, upload_to=get_photo_upload_path, default="ava1.jpg")
    description = models.TextField(null=True, blank=True)
    tags = models.CharField(max_length=256, null=True, blank=True)
    album = models.ForeignKey(Albums, on_delete=models.SET_NULL, null=True, blank=True)
    region = models.ForeignKey(Regions, on_delete=models.SET_NULL, null=True, blank=True)
    brightness = models.CharField(max_length=256, null=True, blank=True)
    contrast = models.CharField(max_length=256, null=True, blank=True)
    rotation = models.CharField(max_length=256, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-id', '-updated']
        verbose_name = 'Uploaded Photo'
        verbose_name_plural = 'Uploaded Photos'

    def __str__(self):
        return str(self.photo)


def get_video_upload_path(instance, filename):
    unique_filename = str(uuid4())  # Генерируем случайное уникальное значение
    return f"videos/{unique_filename}_{filename}"  # Путь для сохранения файла с использованием уникального значения


class UploadedVideos(models.Model):
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    video = models.FileField(null=True, upload_to=get_video_upload_path, default="ava1.jpg")
    cover = models.ImageField(null=True, upload_to='videos/covers', default="favicon.png")
    description = models.TextField(null=True, blank=True)
    tags = models.CharField(max_length=256, null=True, blank=True)
    album = models.ForeignKey(Albums, on_delete=models.SET_NULL, null=True, blank=True)
    region = models.ForeignKey(Regions, on_delete=models.SET_NULL, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-id', '-updated']
        verbose_name = 'Uploaded Video'
        verbose_name_plural = 'Uploaded Videos'

    def __str__(self):
        return str(self.video)
