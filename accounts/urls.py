from django.urls import path
from accounts.views import register

# app_name = 'accounts' # for reverse calls


urlpatterns = [
    path('register/', register, name='register'),
]