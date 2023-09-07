from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

from src.addition.absctract_model import CreatedAt, UpdatedAt, Delete


class Author(CreatedAt, UpdatedAt, Delete):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Album(CreatedAt, UpdatedAt, Delete):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='albums')

    class Meta:
        unique_together = ('title', 'author')

    def __str__(self):
        return self.title


class Song(CreatedAt, UpdatedAt, Delete):
    track_number = models.PositiveIntegerField(unique=True)
    album = models.ForeignKey(Album, on_delete=models.CASCADE, related_name='songs')
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title
