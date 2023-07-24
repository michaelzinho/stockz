import os
from rest_framework import serializers, viewsets, permissions, status
from  rest_framework.response import Response
from ..models import Album
from photos.models import Photo
from .serializers import AlbumSerializers
from django.http import HttpResponseRedirect
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from google_drive import demo as drive

from django.db.models import Q

from django.contrib.auth import get_user_model
User = get_user_model()

class AlbumViewSet (viewsets.ModelViewSet):

    filter_backends = []
    queryset = Album.objects.all()
    serializer_class = AlbumSerializers
    http_method_names = ['get', 'post', 'put', 'delete','head']
    permission_classes = [AllowAny]

    def list(self, request, *args, **kwargs):
        
        if request.user.id == None:
            
            return Response('no user')
        
        user_albuns = Album.objects.filter(Q(owner = request.user.id) | Q(shared_with = request.user.id))
        print(Album.history.all())
        for obj in Album.history.all():
            print(obj, '<<<<')
        serializer = AlbumSerializers(user_albuns, many=True)
        #print(serializer.data, request.user.id, '<<<')
        return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', True)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        
        new_data = request.data
        old_data = instance 
        print(new_data['title'], old_data)
        if new_data['title']:
            if new_data['title'] != old_data.title:
                
                print('seaching for', old_data.title)
                drive.change_file_name(str(old_data.owner.email), old_data.title, new_data['title'])
                
        
        self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            # If 'prefetch_related' has been applied to a queryset, we need to
            # forcibly invalidate the prefetch cache on the instance.
            instance._prefetched_objects_cache = {}

        return Response(serializer.data)

    def create(self, request, *args, **kwargs):

        try:
            owner_data= User.objects.get(id=request.user.id)
          
        except:
            
            return HttpResponseRedirect(redirect_to='http://127.0.0.1:3000/login')
        
        album_request_data = request.data
        
        
        print(request.POST, '<asd\n', request.data,' <asd\n', request)
        
       
        
        nem_album = Album.objects.create(title = album_request_data['title'],
                                         discription = album_request_data['discription'],
                                         owner=owner_data,
                                         #'shared_with = user_list'
                                         )
        
        drive.create_folder(album_request_data['title'], request.user.email)
        #nem_album.save()
        
        image = request.FILES.getlist('photos')
        created_folder_id = drive.get_folder_id( album_request_data['title'])
        
        img_list = list()
        
        if album_request_data['cover']:
            
            cover = request.FILES.getlist('cover') 
            print(cover)
            #input('wait')
        
            img = Photo.objects.create(title = str(cover[0]).replace(" ","_").replace("(","").replace(")","").replace("#","").replace("'","").replace("\"","").replace("+","").replace("!",""),
                                       drive_id = None,
                                       photo = cover[0], #photo = t,
                                       owner = owner_data)
            
            cover_img = Photo.objects.get(id=img.id)
            drive.uploade_data(owner_data, created_folder_id, img.title)
            
            img_list.append(img.title)
            id = drive.get_image(img.title,created_folder_id)
            
            print(id,'<<<<<')
            
            img.drive_id=id
            
            img.save()
            
            nem_album.cover = img
            nem_album.save()
            
        for img in image:

            img = Photo.objects.create(title = str(img).replace(" ","_").replace("(","").replace(")","").replace("#","").replace("'","").replace("\"","").replace("+","").replace("!",""),
                                       drive_id = None,
                                       photo = img, #photo = t,
                                       owner = owner_data)
            
            
            photo = Photo.objects.get(id=img.id)
            nem_album.photos.add(photo)
            
            
            drive.uploade_data(owner_data, created_folder_id, img.title)
            img_list.append(img.title)
            id = drive.get_image(img.title,created_folder_id)
            
            img.drive_id=id
            print(str(img.title), "drive_id=", id)
            img.save()

        try:
            user_list = album_request_data['shared_with']
        except:
            user_list = []
            
        for user in user_list:
            try:
                add_user = User.objects.get(id=user.id)
            except:
                add_user = User.objects.get(id=user)
                
            nem_album.shared_with.add(add_user)
            
        nem_album.save()
        drive.change_permission(created_folder_id) 
        
        for filename in os.listdir('media'):
            print(filename)
            os.remove('media'+'/'+filename)


        serializer = AlbumSerializers(nem_album)
        
        return Response(serializer.data)
         
    def destroy(self, request, pk=None ,*args, **kwargs):
        
        user  = request.user
        folder = instance = self.get_object().title
        
        album = Album.objects.get(id=pk)
        print(user.email, album.title, '<<<<<<')
        drive.delete_folder(user.email, album.title)
        
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)