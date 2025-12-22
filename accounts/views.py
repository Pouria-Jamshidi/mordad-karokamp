from django.shortcuts import render, redirect
from accounts.forms import RegisterForm
from django.contrib import messages

def register(request):
    form = RegisterForm()
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            messages.success(request, f"اکانت {new_user} با موفقیت ساخته شد")
            return redirect('users')
    return render(request, 'accounts/register.html', {'register_form': form})
