from django.contrib.auth.hashers import make_password, acheck_password
from django.shortcuts import render, redirect
from accounts.forms import RegisterForm, LoginForm
from django.contrib import messages
from django.views import View
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth import login, authenticate, logout

User = get_user_model()

def register(request):
    form = RegisterForm()
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            messages.success(request, f"اکانت {new_user} با موفقیت ساخته شد")
            return redirect('users')
    return render(request, 'accounts/register.html', {'register_form': form})

class LoginView(View):
    form = LoginForm()
    def get(self,request):
        form = LoginForm()
        return render(request, 'accounts/login.html', {'login_form': form})
    def post(self,request):
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
        user = authenticate(username=data.get('username'), password=data.get('password'))
        if user:
            login(request, user)
            messages.success(request, "حوش آمدید")
            return redirect('Home')
        else:
            messages.error(request,'کاربری با این مشخصات یافت نشد')
            return render(request, 'accounts/login.html', {'login_form': form})


        # form = LoginForm(request.POST)
        # if form.is_valid():
        #     data = form.cleaned_data
        #     print(data)
        # return redirect('Home')

def logout_view(request):
    logout(request)
    messages.success(request,'شما با موفقیت خارج شدید')
    return redirect('Home')