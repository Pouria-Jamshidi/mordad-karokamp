from django.urls import path
# from core.forms import EditPostForm
from core.views import user_list, posts, main_page, post_detail, new_post, user_detail, delete_post, edit_post, like

# app_name = 'core' #for reverse calls
urlpatterns = [
    path('', main_page, name='Home'),
    path('posts/', posts, name='posts'),
    path('posts/post/<int:post_id>/', post_detail, name='post_detail'),
    path('post/new/', new_post, name='new_post'),
    path('post/edit/<int:post_id>/', edit_post, name='edit_post'),
    path('post/delete/<int:post_id>/',delete_post, name='delete_post'),
    path('users/', user_list, name='users'),
    path('users/user/<int:user_id>/', user_detail, name='user_detail'),
    path("post/like/<int:post_id>/", like, name="like"),

]
