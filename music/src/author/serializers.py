from rest_framework.serializers import ModelSerializer

from src.author.models import Author, Album, Song


class AuthorSerializer(ModelSerializer):

    class Meta:
        model = Author
        fields = ('__all__')


class AlbumSerializer(ModelSerializer):

    class Meta:
        model = Album
        fields = ('__all__')


class SongSerializer(ModelSerializer):

    class Meta:
        model = Song
        fields = ('__all__')