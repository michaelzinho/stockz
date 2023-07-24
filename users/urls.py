
from django.urls import path, include
from users.API.views.GoogleLoginView import GoogleLoginView, UserRedirectView
from dj_rest_auth.views import LoginView, LogoutView

urlpatterns = [
    #dj rest auth | social authentication

    path('google/login', GoogleLoginView.as_view(), name='google_login'),
    path('registration/', include('dj_rest_auth.registration.urls')),
    path('accounts/', include('allauth.urls'), name='socialaccount_signup'),
    path("~redirect/", view=UserRedirectView.as_view(), name="redirect"),
    
]
