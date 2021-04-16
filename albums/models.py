from django.db import models


# Create your models here.
class Album(models.Model):
    song = models.CharField(max_length=50)
    artist = models.CharField(max_length=50)
    album = models.CharField(max_length=50, default=0)
    release_date = models.DateField()
