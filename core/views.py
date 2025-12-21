from django.shortcuts import render, redirect, get_object_or_404
from core.forms import PostForm, NewUser, EditPostForm
from core.models import Post, User
from django.contrib import messages
import os


def main_page(request):
    return render(request, 'core/main.html')


# ===========================================================================================================
# here we have views related to posts
def posts(request):
    p = Post.objects.filter(is_deleted=False)
    return render(request, 'core/posts.html', context={'posts': p})


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
        form = PostForm(request.POST, request.FILES)

        if form.is_valid():
            # =======================================================
            # second way (Django form)
            # data = form.cleaned_data
            # userName = data.pop('username')
            # user = User.objects.filter(username=userName).first()
            # if user:
            #     new_post = Post.objects.create(**data, user=user)
            #     print(new_post.id)
            #     return redirect('posts')

            # =======================================================
            # third way (model form)
            form.save()
            messages.success(request, 'پست شما با موفقیت ثبت شد')
            return redirect('posts')

    return render(request, 'core/new_post.html', {'newPost_form': form})


def delete_post(request, post_id):
    """
    this exists for deleting a post
    it will redirect you to posts page afterward
    :param request:
    :param post_id:
    :return:
    """
    # first usual way
    # post = Post.objects.filter(pk=post_id).first()

    # second way, make sure to import in django.shortcuts
    post = get_object_or_404(Post, pk=post_id)
    # post.delete() # we dont wanna actually delete it so we cant use this
    post.is_deleted = True
    post.save()
    messages.success(request, "حذف شد")
    return redirect('posts')


def edit_post(request, post_id):
    """
    this exists for editing a post and redirect us to the edited post
    :param request:
    :param post_id:
    :return:
    """
    post = get_object_or_404(Post, pk=post_id)
    form = EditPostForm(instance=post)

    # STEP1: adding the address of before edit pic inside so we can remove it of needed afterward
    old_image = post.image

    if request.method == 'POST':
        form = EditPostForm(request.POST, request.FILES, instance=post)
        # user = post.user
        if form.is_valid():
            edited_post = form.save(commit=False)

            # STEP 2: image changed or removed
            if old_image != edited_post.image:
                # delete old image file from disk
                old_path = old_image.path
                if os.path.exists(old_path):
                    os.remove(old_path)

            # way told in class to have a user showin with disable active
            # old = form.save(commit=False)
            # old.user = user
            # old.save()

            edited_post.save()
            messages.success(request, "تغییرات با موفقیت اعمال شد.")
            return redirect('post_detail', post_id=post.id)
    return render(request, 'core/edit_post.html', {'form': form, 'post': post})


# ===========================================================================================================
# here we have views related to users
def user_list(request):
    u = User.objects.all()
    return render(request, 'core/users.html', {'users': u})


def user_detail(request, user_id):
    """
    view function for user details and user_detail URL
    :param request:
    :param int user_id:
    :return:
    """
    userDetail = User.objects.get(pk=user_id)
    return render(request, 'core/user_detail.html', {'user': userDetail})


def new_user(request):
    """
    this is for new_user url
    :param request:
    :return:
    """
    form = NewUser()
    if request.method == 'POST':
        form = NewUser(request.POST)

        if form.is_valid():
            data = form.cleaned_data
            close_friends = data.pop('close_friend')
            new_user = User.objects.create(**data)
            new_user.close_friend.set(close_friends)
            # print(new_user.id)
            return redirect('users')
    return render(request, 'core/new_user.html', {'newUser_form': form})
# ===========================================================================================================
# Create your views here.
