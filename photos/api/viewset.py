from rest_framework import serializers, viewsets
from ..models import Photo
from .serializers import PhotoSerializers,\
                         MultipleImageSerializers
                         
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import api_view, action

class PhotoViewSet (viewsets.ModelViewSet):
    #permission_classes = [IsAuthenticated]
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializers
    http_method_names = ['get', 'post', 'put', 'delete','head']
    
class MultiplePhotosViewSet (viewsets.ModelViewSet):
    #permission_classes = [IsAuthenticated]
    queryset = Photo.objects.all()
    serializer_class = MultipleImageSerializers
    http_method_names = ['get', 'post', 'put', 'delete','head']
    
    @action(detail=False, methods=["POST"]) 
    def multiple_uploads (self,  request, *args, **kwargs):
        serializers = MultipleImageSerializers(data=request.data or None)
        serializers.is_valid()
        image = serializers.validated_data.get("images")
        
        image_list = list()
        
        for image in image_list:
            image_list.append(
                Photo(photo=image)
            )
        
        if image_list:
            Photo.objects.bulk_create(image_list)
            
        return Response("Sucesse")