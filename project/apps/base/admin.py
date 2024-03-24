from django.contrib import admin
from . import models

admin.site.register(models.User)
admin.site.register(models.Albums)
admin.site.register(models.UploadedPhotos)
admin.site.register(models.UploadedVideos)
admin.site.register(models.Regions)
