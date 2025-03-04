
from django.contrib import admin
from .models import Music

@admin.register(Music)
class MusicAdmin(admin.ModelAdmin):
    list_display = ('title', 'artist', 'genre', 'file')
    search_fields = ('title', 'artist', 'genre') 

