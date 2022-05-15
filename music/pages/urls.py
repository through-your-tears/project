from django.urls import path
from . import views


appname = 'pages'
urlpatterns = [
    path('', views.index, name='home'),
    path('song/<int:id>', views.song, name='song'),
    path('add_song', views.add_song, name='add_song'),
    path('artist/<int:id>', views.artist, name='artist'),
    path('add_artist', views.add_artist, name='add_artist'),
    path('add_album', views.add_album, name='add_album'),
    path('album/<int:id>', views.album, name='album'),
    path('add_country', views.add_country, name='add_country')
]