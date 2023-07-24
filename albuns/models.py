from os import path
from django.db import models
from photos.models import Photo
from core import settings
from simple_history.models import HistoricalRecords
from simple_history import register

from django.contrib.auth import get_user_model
User = get_user_model()
register(User)
# Create your models here.

class Album (models.Model):

    title = models.CharField(("Titulo"), max_length=50)
    discription = models.CharField(("Descrição"), max_length=500)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name=("Dono"), on_delete=models.CASCADE)
    shared_with = models.ManyToManyField(settings.AUTH_USER_MODEL, verbose_name=("Compartilhado com"), related_name="album_shared_with")
    create_date = models.DateTimeField(("Data de criação"), auto_now_add=True) 
    cover = models.ForeignKey(Photo, related_name='Cover_album', on_delete=models.SET_NULL, blank=True, null=True)
    photos = models.ManyToManyField(Photo, verbose_name=("Fotos"), blank=True, null=True)
    last_modified = models.DateTimeField(("Ultima alteração"), auto_now=True)  
    delete_on_reset_day = models.BooleanField(("Deletar no dia de exclusão"), default=False)
    history = HistoricalRecords()
    
    
    verbose_name = 'Album'
    verbose_name_plural = 'Albuns'

    def __str__ (self):

        return self.title
