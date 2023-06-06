from django.contrib import admin
from django.urls import path, include
from users.API.views.GoogleLoginView import GoogleLoginView, UserRedirectView
from rest_framework.schemas  import get_schema_view
from rest_framework.routers import DefaultRouter
from django.conf.urls.static import static
from django.conf import settings

from drf_spectacular.views import (
    SpectacularAPIView, 
    SpectacularRedocView,
    SpectacularSwaggerView
)

from albuns.api.viewset import AlbumViewSet
from photos.api.viewset import PhotoViewSet, MultiplePhotosViewSet


router = DefaultRouter()
router.register(r'album', AlbumViewSet, basename='Album')
router.register(r'singlephoto', PhotoViewSet, basename='Photo')
router.register(r'multiplephotos', MultiplePhotosViewSet, basename='Photos')



urlpatterns = [
    path('admin/', admin.site.urls),
    
    #dj rest auth | authentication
    path('user/', include('dj_rest_auth.urls')),
    path('user/registration/', include('dj_rest_auth.registration.urls')),

    #dj rest auth | social authentication
    path('', include('users.urls')),
    
    #api
    path('api/', include(router.urls)),
    
    #spectacular | docs
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/doc/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
