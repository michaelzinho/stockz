from django.contrib import admin
from .models import CustomUser
from simple_history.admin import SimpleHistoryAdmin
# Register your models here.
admin.site.register(CustomUser, SimpleHistoryAdmin)