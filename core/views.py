from django.shortcuts import render

from core.models import Post,User


def jadid(request):
    p=Post.objects.all()
    return render(request, 'core/home.html', context={'posts':p})

def user_list(request):
    u = User.objects.all()
    return render(request,'core/users.html',{'users':u})

def main_page(request):
    return render(request,'core/main.html')
# Create your views here.
