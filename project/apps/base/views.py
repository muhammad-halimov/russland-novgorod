from django.shortcuts import render, redirect
from . import models
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q
from django.contrib.auth import authenticate, login, logout
from . import forms
from .coreutils import detect_objects
import re
import json
from django.http import JsonResponse


def main(request):
    photo = models.UploadedPhotos.objects.all()
    video = models.UploadedVideos.objects.all()

    context = {'photos': photo, 'videos': video}
    return render(request, 'base/main.htm', context)


def login_page(request):
    if request.user.is_authenticated:
        return redirect('main')

    if request.method == 'POST':
        email = request.POST.get('email').lower()
        password = request.POST.get('password')

        # noinspection PyBroadException
        try:
            models.User.objects.get(email=email)
        except BaseException:
            messages.error(request, "Пароль или Почта неправльная")

        user = authenticate(request, email=email, password=password)

        # noinspection PyBroadException
        try:
            login(request, user)
            return redirect('main')
        except BaseException:
            messages.error(request, "Просто неправильный ответ...")  # Don't touch it

    return render(request, 'base/login.htm')


def registration_page(request):
    if request.user.is_authenticated:
        return redirect('main')

    form = forms.UnterUserCreationForm

    if request.method == 'POST':
        form = forms.UnterUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            form.save()
            login(request, user)
            return redirect('main')
        else:
            messages.error(request, 'Возникла ошибка в процессе регистрации')
            messages.error(request, 'Либо пароль слишком слабый')

    context = {'form': form}
    return render(request, 'base/registration.htm', context)


@login_required(login_url='main')
def logout_page(request):
    logout(request)
    return redirect('main')


@login_required(login_url='login')
def profile(request):
    # noinspection PyBroadException
    try:
        user_photos = models.UploadedPhotos.objects.filter(owner=request.user)
        user_videos = models.UploadedVideos.objects.filter(owner=request.user)
        user_albums = models.Albums.objects.filter(owner=request.user)
    except BaseException:
        user_photos = ''
        user_videos = ''
        user_albums = ''

    context = {
        'user_photos': user_photos,
        'user_videos': user_videos,
        'user_albums': user_albums
    }

    return render(request, 'base/profile.htm', context)


def user_profile(request, pk):
    user = models.User.objects.get(id=pk)

    if request.user.id == user.id:
        return redirect('profile')

    # noinspection PyBroadException
    try:
        user_photos = models.UploadedPhotos.objects.filter(owner=user.id)
        user_videos = models.UploadedVideos.objects.filter(owner=user.id)
        user_albums = models.Albums.objects.filter(owner=user.id)
    except BaseException:
        user_photos = ''
        user_videos = ''
        user_albums = ''

    context = {
        'user_photos': user_photos,
        'user_videos': user_videos,
        'user_albums': user_albums,
        'user': user,
    }
    return render(request, 'base/profile.htm', context)


@login_required(login_url='login')
def edit_profile(request, pk):
    user = models.User.objects.get(id=pk)
    form = forms.UserEditForm(request.POST or None, request.FILES or None, instance=user)

    if request.method == 'POST':
        if form.is_valid():
            form.avatar_brightness = request.POST.get('brightness')
            form.avatar_contrast = request.POST.get('contrast')
            form.avatar_rotation = request.POST.get('rotation')
            form.save()
            return redirect('user_profile', pk=user.id)

    context = {'user': user, 'form': form}
    return render(request, 'base/components/edit_profile.htm', context)


@login_required(login_url='login')
def upload_photo(request):
    form = forms.PhotoForm

    if request.method == 'POST':
        form = forms.PhotoForm(request.POST or None, request.FILES or None)
        # path_pattern = 'project/static/uploads/photos/0baf04d9-65c6-45fa-af4d-a21f4e4943a8_ww.jpg'

        if form.is_valid():
            photo = form.save(commit=False)
            photo.owner = request.user
            photo.brightness = request.POST.get('brightness')
            photo.contrast = request.POST.get('contrast')
            photo.rotation = request.POST.get('rotation')
            form.save()
            photo.tags = detect_objects(f"project/static{str(photo.photo.url)}")
            form.save()

        return redirect('photos')

    context = {'form': form}
    return render(request, 'base/components/upload_photo.htm', context)


@login_required(login_url='login')
def upload_video(request):
    form = forms.VideoForm

    if request.method == 'POST':
        form = forms.VideoForm(request.POST or None, request.FILES or None)

        if form.is_valid():
            video = form.save(commit=False)
            video.owner = request.user
            form.save()
            video.tags = detect_objects(f"project/static{str(video.cover.url)}")
            form.save()

        return redirect('videos')

    context = {'form': form}
    return render(request, 'base/components/upload_video.htm', context)


@login_required(login_url='login')
def create_album(request):
    form = forms.AlbumForm

    if request.method == 'POST':
        form = forms.AlbumForm(request.POST or None, request.FILES or None)

        if form.is_valid():
            album = form.save(commit=False)
            album.owner = request.user
            album.brightness = request.POST.get('brightness')
            album.contrast = request.POST.get('contrast')
            album.rotation = request.POST.get('rotation')
            form.save()
            album.tags = detect_objects(f"project/static{str(album.photo.url)}")
            form.save()
            form.save_m2m()

        return redirect('albums')

    context = {'form': form}
    return render(request, 'base/components/create_album.htm', context)


def s_photo(request, pk):
    single_photo = models.UploadedPhotos.objects.get(id=pk)

    context = {'photo': single_photo}
    return render(request, 'base/single_photo.htm', context)


def s_video(request, pk):
    single_video = models.UploadedVideos.objects.get(id=pk)

    context = {'video': single_video}
    return render(request, 'base/single_video.htm', context)


def s_album(request, pk):
    single_album = models.Albums.objects.get(id=pk)

    if not single_album.status and request.user != single_album.owner:
        return redirect('main')

    context = {'album': single_album}
    return render(request, 'base/single_album.htm', context)


def photos(request):
    photo = models.UploadedPhotos.objects.all()

    context = {'photos': photo}
    return render(request, 'base/photos.htm', context)


def videos(request):
    video = models.UploadedVideos.objects.all()

    context = {'videos': video}
    return render(request, 'base/videos.htm', context)


def albums(request):
    album = models.Albums.objects.all()

    context = {'albums': album}
    return render(request, 'base/albums.htm', context)


@login_required(login_url='login')
def edit_photo(request, pk):
    photo = models.UploadedPhotos.objects.get(id=pk)
    form = forms.PhotoForm(request.POST or None, request.FILES or None, instance=photo)

    if request.method == 'POST':
        if form.is_valid():
            x_photo = form.save(commit=False)
            x_photo.brightness = request.POST.get('brightness')
            x_photo.contrast = request.POST.get('contrast')
            x_photo.rotation = request.POST.get('rotation')
            form.save()
            return redirect('photo', pk=photo.id)

    context = {'photo': photo, 'form': form}
    return render(request, 'base/components/edit_photo.htm', context)


@login_required(login_url='login')
def edit_video(request, pk):
    video = models.UploadedVideos.objects.get(id=pk)
    form = forms.VideoForm(request.POST or None, request.FILES or None, instance=video)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('videos')

    context = {'video': video, 'form': form}
    return render(request, 'base/components/edit_video.htm', context)


@login_required(login_url='login')
def edit_album(request, pk):
    album = models.Albums.objects.get(id=pk)
    form = forms.AlbumForm(request.POST or None, request.FILES or None, instance=album)

    if request.method == 'POST':
        if form.is_valid():
            x_album = form.save(commit=False)
            x_album.brightness = request.POST.get('brightness')
            x_album.contrast = request.POST.get('contrast')
            x_album.rotation = request.POST.get('rotation')
            form.save()
            return redirect('album', pk=album.id)

    context = {'album': album, 'form': form}
    return render(request, 'base/components/edit_album.htm', context)


@login_required(login_url='login')
def delete_photo(request, pk):
    if request.user != models.UploadedPhotos.objects.get(id=pk).owner:
        return redirect('main')
    else:
        models.UploadedPhotos.objects.get(id=pk).delete()
        return redirect('profile')


@login_required(login_url='login')
def delete_video(request, pk):
    if request.user != models.UploadedVideos.objects.get(id=pk).owner:
        return redirect('main')
    else:
        models.UploadedVideos.objects.get(id=pk).delete()
        return redirect('profile')


@login_required(login_url='login')
def delete_album(request, pk):
    if request.user != models.Albums.objects.get(id=pk).owner:
        return redirect('main')
    else:
        models.Albums.objects.get(id=pk).delete()
        return redirect('profile')


def search(request):
    full_query = request.GET.get('query') if request.GET.get('query') else ''
    query = request.GET.get('query')[:4] if request.GET.get('query') else ''

    pattern = re.sub(r'[ _-]', r'[ _-]', query)

    photo = models.UploadedPhotos.objects.filter(Q(tags__regex=pattern))
    video = models.UploadedVideos.objects.filter(Q(tags__regex=pattern))
    album = models.Albums.objects.filter(Q(tags__iregex=pattern))

    general = int(photo.count() + video.count() + album.count())

    context = {
        'photos': photo,
        'videos': video,
        'albums': album,
        'full_query': full_query,
        'general': general
    }
    return render(request, 'base/search.htm', context)


def map_ajax(request):
    data = json.loads(request.body)
    region = data['region'][:4] or ''

    return JsonResponse({'region': region}, safe=False)


@login_required(login_url='login')
def map_page(request, region):
    photo = models.UploadedPhotos.objects.filter(Q(region__name__icontains=region))

    context = {'photos': photo}
    return render(request, 'base/map.htm', context)
