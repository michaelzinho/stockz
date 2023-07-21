from rest_framework import serializers, viewsets
from ..models import Photo
from .serializers import PhotoSerializers,\
                         MultipleImageSerializers
                         
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import api_view, action

from django.contrib.auth import get_user_model
User = get_user_model()

class PhotoViewSet (viewsets.ModelViewSet):
    #permission_classes = [IsAuthenticated]
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializers
    http_method_names = ['get', 'post', 'put', 'delete','head']
    #permission_classes = [IsAuthenticated]
    
    def create (self,  request, *args, **kwargs):
        
        try:
            owner_data= User.objects.get(request.user.id)
        except:
            print('no_user logged in default selected')
            owner_data = User.objects.get(id=1)
        photo_request_data = request.data
        teste = request.FILES.getlist('photo')
        
        
        print(teste, '><><><>')
        for imagem, t in zip(photo_request_data['photo'], teste):
            img = Photo.objects.create(title = t,
                                       discription = None,
                                       photo = t,
                                       owner = owner_data)
            img.save()
            print('imagem salva')
            
        return Response("Sucesse")
    
class MultiplePhotosViewSet (viewsets.ModelViewSet):
    #permission_classes = [IsAuthenticated]
    queryset = Photo.objects.all()
    serializer_class = MultipleImageSerializers
    http_method_names = ['get', 'post', 'put', 'delete','head']
    #permission_classes = [IsAuthenticated]
    
    
    
    def create (self,  request, *args, **kwargs):
        serializers = MultipleImageSerializers(data=request.data or None)
        serializers.is_valid()
        images = serializers.validated_data.get("images")
        
        image_list = list()
        input('wait >>>>>')
        for image in images:
            input(image, '<<<<')
            image_list.append(
                Photo(photo=image)
            )
        
        if image_list:
            Photo.objects.bulk_create(image_list)
            
        return Response("Sucesse")