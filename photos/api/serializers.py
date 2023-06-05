from albuns.models import Album
from rest_framework import serializers
from ..models import Photo

class PhotoSerializers (serializers.ModelSerializer):

    class Meta:

        model = Photo
        fields = ['title', 'discription', 'photo', 'owner', 'shared_with']

        
class MultipleImageSerializers (serializers.Serializer):
    
    photo = serializers.ListField(
        child = serializers.ImageField()
    )