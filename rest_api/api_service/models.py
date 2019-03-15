from django.db import models

# Create your models here.
class PlayList(models.Model):
    song = models.CharField(max_length = 50)
    album = models.CharField(max_length = 50)
    artist = models.CharField(max_length = 50)
    release_date = models.DateField()

    def __str__(self):
        return self.song
