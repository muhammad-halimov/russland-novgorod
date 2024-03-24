from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('login', views.login_page, name='login'),
    path('registration', views.registration_page, name='registration'),
    path('logout', views.logout_page, name='logout'),
    path('profile', views.profile, name='profile'),
    path('edit_profile/<str:pk>', views.edit_profile, name='edit_profile'),
    path('user_profile/<str:pk>', views.user_profile, name='user_profile'),
    path('upload_photo', views.upload_photo, name='upload_photo'),
    path('upload_video', views.upload_video, name='upload_video'),
    path('create_album', views.create_album, name='create_album'),
    path('edit_album/<str:pk>', views.edit_album, name='edit_album'),
    path('edit_photo/<str:pk>', views.edit_photo, name='edit_photo'),
    path('edit_video/<str:pk>', views.edit_video, name='edit_video'),
    path('delete_photo/<str:pk>', views.delete_photo, name='delete_photo'),
    path('delete_video/<str:pk>', views.delete_video, name='delete_video'),
    path('delete_album/<str:pk>', views.delete_album, name='delete_album'),
    path('photos', views.photos, name='photos'),
    path('videos', views.videos, name='videos'),
    path('albums', views.albums, name='albums'),
    path('photo/<str:pk>', views.s_photo, name='photo'),
    path('video/<str:pk>', views.s_video, name='video'),
    path('album/<str:pk>', views.s_album, name='album'),
    path('search', views.search, name='search'),
    path('map', views.map_page, name='map'),
]
