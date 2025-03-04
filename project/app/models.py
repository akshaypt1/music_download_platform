from django.db import models
from django.utils.timezone import now 

class User(models.Model):
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=200)  # You may hash passwords later
    date_joined = models.DateTimeField(default=now)

    def __str__(self):
        return self.username

class Genre(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Artist(models.Model):
    name = models.CharField(max_length=255)
    # bio = models.TextField(blank=True, null=True)
    profile_image = models.ImageField(upload_to='artists/', blank=True, null=True)

    def __str__(self):
        return self.name

# class Album(models.Model):
#     title = models.CharField(max_length=255)
#     artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
#     release_date = models.DateField()
#     cover_image = models.ImageField(upload_to='albums/', blank=True, null=True)

#     def _str_(self):
#         return self.title

class Music(models.Model):
    title = models.CharField(max_length=255)
    artist = models.CharField(max_length=255)
    genre = models.CharField(max_length=100)
    file = models.FileField(upload_to='music/')
    cover_image = models.ImageField(upload_to='covers/', blank=True, null=True)
    popularity = models.IntegerField(default=0)
    is_trending = models.BooleanField(default=False)
    upload_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
