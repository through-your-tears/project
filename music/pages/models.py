from django.db import models


class Country(models.Model):
    name = models.CharField(max_length=100, verbose_name='страна', unique=True)

    def __str__(self):
        return self.name


class Artist(models.Model):
    name = models.CharField(max_length=100, verbose_name='страна')
    country = models.ForeignKey(Country, verbose_name='страна', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name


class Album(models.Model):
    name = models.CharField(max_length=100, verbose_name='альбом')
    number = models.IntegerField(verbose_name='количество песен в альбоме')
    artist = models.ForeignKey(Artist, verbose_name='исполнитель', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Song(models.Model):
    name = models.CharField(max_length=200, verbose_name='название песни')
    length = models.IntegerField(verbose_name='длина песни в секундах')
    artist = models.ForeignKey(Artist, verbose_name='исполнитель', on_delete=models.SET_NULL, null=True)
    album = models.ForeignKey(Album, verbose_name='альбом', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name
