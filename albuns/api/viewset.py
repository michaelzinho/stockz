from rest_framework import serializers, viewsets, permissions
from ..models import Album
from .serializers import AlbumSerializers
from rest_framework.permissions import IsAuthenticated


class AlbumViewSet (viewsets.ModelViewSet):

    queryset = Album.objects.all()
    serializer_class = AlbumSerializers
    http_method_names = ['get', 'post', 'put', 'delete','head']
    permission_classes = [IsAuthenticated]
