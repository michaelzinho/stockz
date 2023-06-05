from django.contrib import admin
from django.urls import path, include

from drf_spectacular.views import (
    SpectacularAPIView, 
    SpectacularRedocView,
    SpectacularSwaggerView
)

urlpatterns = [
    path('admin/', admin.site.urls),

    #dj rest auth | authentication
    path('user/', include('dj_rest_auth.urls')),
    path('user/registration/', include('dj_rest_auth.registration.urls')),

    #spectacular | docs
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/doc/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),

]
