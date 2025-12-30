from django.contrib.auth.views import LogoutView
from django.urls import path
from accounts.views import register, LoginView, logout_view, user_list, profile

# app_name = 'accounts' # for reverse calls


urlpatterns = [
    path('register/', register, name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/',logout_view, name='logout'),
    path('users/', user_list, name='users'),
    path('profile/<int:user_id>/', profile, name='profile'),
]