from django.contrib.auth.views import LogoutView
from django.urls import path
from accounts.views import register, LoginView, logout_view

# app_name = 'accounts' # for reverse calls


urlpatterns = [
    path('register/', register, name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/',logout_view, name='logout'),
]