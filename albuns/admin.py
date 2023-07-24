from django.contrib import admin
from simple_history.admin import SimpleHistoryAdmin
from .models import Album
# Register your models here.


admin.site.register(Album, SimpleHistoryAdmin)