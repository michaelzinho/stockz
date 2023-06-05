from django.contrib import admin
from django.urls import path, include
from users.API.views.GoogleLoginView import GoogleLoginView, UserRedirectView

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

    #dj rest auth | social authentication
    path('user/google/login', GoogleLoginView.as_view(), name='google_login'),
    path('dj-rest-auth/registration/', include('dj_rest_auth.registration.urls')),
    path('accounts/', include('allauth.urls'), name='socialaccount_signup'),
    path("~redirect/", view=UserRedirectView.as_view(), name="redirect"),
    #spectacular | docs
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/doc/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),

]
