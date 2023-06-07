from rest_framework import serializers, viewsets
from ..models import Album
from .serializers import AlbumSerializers

class AlbumViewSet (viewsets.ModelViewSet):

    queryset = Album.objects.all()
    serializer_class = AlbumSerializers
    http_method_names = ['get', 'post', 'put', 'delete','head']
    
