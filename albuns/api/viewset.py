from rest_framework import serializers, viewsets, permissions
from  rest_framework.response import Response
from ..models import Album
from photos.models import Photo
from .serializers import AlbumSerializers
from rest_framework.permissions import IsAuthenticated

from django.contrib.auth import get_user_model
User = get_user_model()

class AlbumViewSet (viewsets.ModelViewSet):

    queryset = Album.objects.all()
    serializer_class = AlbumSerializers
    http_method_names = ['get', 'post', 'put', 'delete','head']
    #permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        
        try:
            owner_data= User.objects.get(request.user.id)
        except:
            print('no_user logged in')
            owner_data = User.objects.get(id=1)
        
        album_request_data = request.data
        print('>>> aquiiiiiii',album_request_data['cover'],' >>>',
              album_request_data['photos'])
        
        print(request.POST, '<asd\n', request.data,' <asd\n', request)
        
        get_album_cover = Photo.objects.get(id=album_request_data['cover'])
        
        if get_album_cover:      
            albumCover = get_album_cover
        else: 
            albumCover = None
            
        
        nem_album = Album.objects.create(title = album_request_data['title'],
                                         discription = album_request_data['discription'],
                                         owner=owner_data,
                                         cover = albumCover
                                         #shared = 'user_list'
                                         )
        
        nem_album.save()
        
        
        for foto_id in album_request_data['photos']:
            photo = Photo.objects.get(id=foto_id)
            nem_album.photos.add(photo)
        
        serializer = AlbumSerializers(nem_album)
        
        return Response(serializer.data)
                               
         