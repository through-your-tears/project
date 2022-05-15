from django.shortcuts import render, redirect, HttpResponse
from .models import Country, Album, Artist, Song
from .forms import CountryForm, AlbumForm, ArtistForm, SongForm


# Create your views here.


def index(request):
    ctx = {
        'countries': Country.objects.all(),
        'albums': Album.objects.all(),
        'artists': Artist.objects.all(),
        'songs': Song.objects.all()
    }
    return render(request, 'pages/index.html', ctx)


def add_country(request):
    if request.POST:
        form = CountryForm(request.POST)
        if form.is_valid():
            form.save()
            redirect('home')
        else:
            return HttpResponse('Форма введена с ошибкой')
    else:
        form = CountryForm()
    ctx = {
        'form': form
    }
    return render(request, 'pages/add_country.html', ctx)


def album(request, id):
    alb = Album.objects.get(pk=id)
    if request.POST:
        form = AlbumForm(request.POST)
        if form.is_valid():
            alb.name = form.cleaned_data['name']
            alb.number = form.cleaned_data['number']
            alb.artist = form.cleaned_data['artist']
            alb.save(update_fields=['name', 'number', 'artist'])
        else:
            return HttpResponse('Форма введена с ошибкой')
    form = AlbumForm()
    ctx = {
        'album': alb,
        'form': form
    }
    return render(request, 'pages/album.html', ctx)


def add_album(request):
    if request.POST:
        form = AlbumForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            return HttpResponse('Форма введена с ошибкой')
    else:
        form = AlbumForm()
    ctx = {
        'form': form
    }
    return render(request, 'pages/add_album.html', ctx)


def artist(request, id):
    art = Artist.objects.get(pk=id)
    if request.POST:
        form = ArtistForm(request.POST)
        if form.is_valid():
            art.name = form.cleaned_data['name']
            art.country = form.cleaned_data['country']
            art.save(update_fields=['name', 'country'])
        else:
            return HttpResponse('Форма введена с ошибкой')
    form = ArtistForm()
    ctx = {
        'artist': art,
        'form': form
    }
    return render(request, 'pages/artist.html', ctx)


def add_artist(request):
    if request.POST:
        form = ArtistForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            return HttpResponse('Форма введена с ошибкой')
    else:
        form = ArtistForm()
    ctx = {
        'form': form
    }
    return render(request, 'pages/add_artist.html', ctx)


def song(request, id):
    s = Song.objects.get(pk=id)
    if request.POST:
        form = SongForm(request.POST)
        if form.is_valid():
            s.name = form.cleaned_data['name']
            s.length = form.cleaned_data['length']
            s.artist = form.cleaned_data['artist']
            s.album = form.cleaned_data['album']
            s.save(update_fields=['name', 'length', 'artist', 'album'])
        else:
            return HttpResponse('Форма введена с ошибкой')
    form = SongForm()
    ctx = {
        'song': s,
        'form': form
    }
    return render(request, 'pages/song.html', ctx)


def add_song(request):
    if request.POST:
        form = SongForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            return HttpResponse('Форма введена с ошибкой')
    else:
        form = SongForm()
    ctx = {
        'form': form
    }
    return render(request, 'pages/add_song.html', ctx)
