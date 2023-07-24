from django.db import models
from core import settings
from simple_history.models import HistoricalRecords

# Create your models here.

class Photo (models.Model):
    #album.set_photos

    title = models.CharField(("Titulo"), blank=True, null=True, max_length=8050)
    drive_id = models.CharField(("Descrição"), blank=True, null=True, max_length=500)
    photo = models.ImageField(("Foto"), upload_to='', height_field=None, width_field=None, max_length=None, blank=True, null=True,)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name=("Dono"), on_delete=models.CASCADE)
    history = HistoricalRecords()
    #shared_with = models.ManyToManyField(settings.AUTH_USER_MODEL, verbose_name=("Compartilhado com"), related_name="photo_shared_with")
    
    verbose_name = 'Photo'
    verbose_name_plural = 'Photos'
    
    def __str__ (self):
        return self.title