from django.shortcuts import render,redirect
from core.forms import PostForm
from core.models import Post, User


def posts(request):
    p = Post.objects.all()
    return render(request, 'core/posts.html', context={'posts': p})


def user_list(request):
    u = User.objects.all()
    return render(request, 'core/users.html', {'users': u})


def main_page(request):
    return render(request, 'core/main.html')


# Create your views here.
def post_detail(request, post_id):
    post = Post.objects.get(pk=post_id)
    return render(request, 'core/post_detail.html', {'post': post})


def new_post(request):
    # if request.method == "POST":
    #     form_data = request.POST
    #     title=form_data.get('title')
    #     content=form_data.get('content')
    #     userName=form_data.get('user')
    #     category=form_data.get('category')
    #     user=User.objects.filter(username=userName).first()
    #     if user:
    #         Post.objects.create(title=title, content=content, user=user, category=category)
    #     else:
    #         pass
    form = PostForm()
    if request.method == 'POST':
        form = PostForm(request.POST)



        if form.is_valid():
            data = form.cleaned_data
            userName = data.pop('username')
            user = User.objects.filter(username=userName).first()
            if user:
                new_post = Post.objects.create(**data, user=user)
                print(new_post.id)
                return redirect('posts')

    return render(request, 'core/new_post.html', {'newPost_form': form})
