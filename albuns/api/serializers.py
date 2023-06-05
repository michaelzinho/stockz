from rest_framework import serializers
from ..models import Album
from photos.api.serializers import PhotoSerializers

class AlbumSerializers (serializers.ModelSerializer):
    class Meta:

        model = Album
        fields = ['title', 'discription', 'owner', 'shared_with', 'create_date', 'photos', 'delete_on_reset_day']      