from django.forms import ModelForm, MultipleChoiceField
from django.contrib.auth.forms import UserCreationForm
from . import models
from django import forms


class UnterUserCreationForm(UserCreationForm):
    class Meta:
        model = models.User
        fields = ['username', 'email', 'login', 'password1', 'password2']


class UserEditForm(ModelForm):
    class Meta:
        model = models.User
        fields = ['username', 'email', 'login', 'avatar']
        widgets = {
            'avatar': forms.FileInput(attrs={'accept': 'image/*,.png,.jpg', 'id': 'id_photo'}),
        }


class PhotoForm(ModelForm):
    class Meta:
        model = models.UploadedPhotos
        fields = '__all__'
        exclude = ['owner', 'created', 'updated']
        widgets = {
            'photo': forms.FileInput(attrs={'accept': 'image/*,.dng,.raw'}),
            'album': forms.Select(),
            'region': forms.Select(),
        }


class VideoForm(ModelForm):
    class Meta:
        model = models.UploadedVideos
        fields = '__all__'
        exclude = ['owner', 'created', 'updated']
        widgets = {
            'video': forms.FileInput(attrs={'accept': 'video/*'}),
            'cover': forms.FileInput(attrs={'accept': 'image/*,.png,.jpg'}),
            'album': forms.Select(),
            'region': forms.Select(),
        }


class AlbumForm(ModelForm):
    class Meta:
        model = models.Albums
        fields = '__all__'
        exclude = ['owner', 'created', 'updated']
        widgets = {
            'photo': forms.FileInput(attrs={'accept': 'image/*,.dng,.raw'}),
            'coauthors': forms.SelectMultiple(attrs={'id': 'select_options'}),
            'status': forms.CheckboxInput()
        }
