from django.db.models import F,Count
from django.shortcuts import render, redirect, get_object_or_404
from core.forms import PostForm, EditPostForm
from core.models import Post,Like
from accounts.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required

import os



def main_page(request):
    return render(request, 'core/main.html')


# ===========================================================================================================
# here we have views related to posts
def posts(request):
    p = Post.objects.filter(is_deleted=False)
    return render(request, 'core/posts.html', context={'posts': p})


def post_detail(request, post_id):
    '''
    view function for details of a certain post and 'post_detail' URL
    :param request:
    :param post_id:
    :return:
    '''
    post = get_object_or_404(Post.objects.annotate(
        like_count=Count(F('post_likes'))), pk=post_id)
    is_liked = post.post_likes.filter(user=request.user).exists()  # So the icon changes depending on whether or not it is liked.
    return render(request, 'core/post_detail.html', {'post': post,'is_liked': is_liked})

@login_required
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

    # if request.user.is_authenticated:
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
            newPost = form.save(commit=False)
            newPost.user = request.user
            newPost.save()
            messages.success(request, 'پست شما با موفقیت ثبت شد')
            return redirect('posts')

    return render(request, 'core/new_post.html', {'newPost_form': form})
    # else:
    #     messages.error(request,"برای دیدن این صفحه ورود کنید")
    #     return redirect('login')

@login_required
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
    if post.user == request.user or request.user.is_superuser: #only allowed for post's original user or superusers
        post.is_deleted = True
        post.save()
        messages.success(request, "حذف شد")
        return redirect('posts')
    else:
        return redirect('post_detail', post_id=post_id)

@login_required
def edit_post(request, post_id):
    """
    view function for editing a post and 'edit_post' URL.
    :param request:
    :param post_id:
    :return:
    """
    post = get_object_or_404(Post, pk=post_id)
    form = EditPostForm(instance=post)

    if request.user == post.user or request.user.is_superuser:
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

    else:
        messages.error(request, 'این پست شما نیست نمیتوانید روی آن تغییر انجام دهید')
        return redirect('post_detail', post_id=post.id)



def like(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    if request.method == 'POST':
        like,created = Like.objects.update_or_create(user=request.user, post=post) # If liked is created, created return True, if updated, it returns False
        if not created:
            like.delete()
    return redirect('post_detail', post_id=post_id)
