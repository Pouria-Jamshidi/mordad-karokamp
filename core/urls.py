from django.urls import path
from core.views import user_list,jadid,main_page

urlpatterns = [
    path('',main_page,name='main page'),
    path('posts/',jadid,name='posts'),
    path('users/',user_list,name='users'),

]