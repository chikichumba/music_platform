from django.db import models
from django.utils.text import slugify

class Song(models.Model):
    name = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(f"{self.name}-{self.author}")
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.name} - {self.author}"
    

class Geners(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(f"{self.name}-{self.author}")
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
    

class Artist(models.Model):
    name = models.CharField(max_length=100, unique=True)
    photo = models.ImageField(upload_to='artists/', null=True, blank=True)
    slug = models.SlugField(max_length=100, unique=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(f"{self.name}-{self.author}")
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
    

class Album(models.Model):
    title = models.CharField(max_length=100)
    artist = models.ForeignKey(
        Artist, 
        on_delete=models.CASCADE, 
        related_name='albums'
    )
    release_date = models.DateField()
    cover = models.ImageField(upload_to='albums/', null=True, blank=True)
    slug = models.SlugField(max_length=100, unique=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(f"{self.title}-{self.artist.name}")
        super().save(*args, **kwargs)
    
    def __str__(self):
        return f"{self.title} - {self.artist.name}"
