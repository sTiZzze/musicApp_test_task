from rest_framework import routers
from django.urls import path, include

from src.author.views import Author, Album, Song

router = routers.DefaultRouter()
router.register('author', Author, "author")
router.register('album', Album, "album")
router.register('song', Song, "song")

urlpatterns = [
    path('', include(router.urls)),
]

urlpatterns += router.urls