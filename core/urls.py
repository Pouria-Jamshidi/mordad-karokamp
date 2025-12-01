from django.urls import path
from core.views import user_list, posts, main_page, post_detail, new_post

urlpatterns = [
    path('', main_page, name='Home'),
    path('posts/', posts, name='posts'),
    path('users/',user_list,name='users'),
    path('posts/post/<int:post_id>/',post_detail,name='post_detail'),
    path('post/new/',new_post,name='new_post'),

]