from django.contrib import admin
from .models import Photo
from simple_history.admin import SimpleHistoryAdmin
# Register your models here.

admin.site.register(Photo, SimpleHistoryAdmin)