from django.contrib import admin
from .models import Song, Geners, Artist, Album

@admin.register
class SongAdmin(admin.ModelAdmin):
    list_display = ['name', 'author', 'genre']
    prepopulated_fields = {'slug': ('name', 'author')}

@admin.register
class GenersAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}

@admin.register
class AdminArtist(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}

@admin.register
class AdminAlbum(admin.ModelAdmin):
    list_display = ['title','artist','slug']
    prepopulated_fields = {'slug': ('title', 'artist')}