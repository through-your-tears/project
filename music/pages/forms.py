from django.forms import ModelForm

from .models import Country, Album, Artist, Song


class CountryForm(ModelForm):

    class Meta:
        model = Country
        fields = ('name',)


class ArtistForm(ModelForm):

    class Meta:
        model = Artist
        fields = ('name', 'country')


class AlbumForm(ModelForm):

    class Meta:
        model = Album
        fields = ('name', 'number', 'artist')


class SongForm(ModelForm):

    class Meta:
        model = Song
        fields = ('name', 'length', 'artist', 'album')
