from django.shortcuts import render

from core.models import Post,User


def posts(request):
    p=Post.objects.all()
    return render(request, 'core/posts.html', context={'posts':p})

def user_list(request):
    u = User.objects.all()
    return render(request,'core/users.html',{'users':u})

def main_page(request):
    return render(request,'core/main.html')
# Create your views here.
def post_detail(request,post_id):
    post = Post.objects.get(pk=post_id)
    return render(request, 'core/post_detail.html', {'post':post})

def new_post(request):
    return render(request, 'core/new_post.html')