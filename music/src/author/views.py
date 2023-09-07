from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet

from src.author.serializers import AuthorSerializer, AlbumSerializer, SongSerializer
from src.author.models import Author, Album, Song


class Author(mixins.ListModelMixin, mixins.CreateModelMixin, GenericViewSet):

    serializer_class = AuthorSerializer
    queryset = Author.objects.all()

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class Album(mixins.ListModelMixin, mixins.CreateModelMixin, GenericViewSet):

    serializer_class = AlbumSerializer
    queryset = Album.objects.all()

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class Song(mixins.ListModelMixin, mixins.CreateModelMixin, GenericViewSet):

    serializer_class = SongSerializer
    queryset = Song.objects.all()

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)