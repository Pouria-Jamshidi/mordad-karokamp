from django import forms
from django.contrib.auth import get_user_model


# from accounts.models import User #first way of doing RegisterForm
from django.core.exceptions import ValidationError
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm #second way of RegisterForm and LoginForm

User = get_user_model() #second way of RegisterForm and LoginForm else the auth wont recognize the new setting we did in faceboom python dir and page crashes.

#first way of RegisterForm
class RegisterForm(forms.ModelForm):
    p1 = forms.CharField(max_length=30,label="گذرواژه" ,widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    p2 = forms.CharField(max_length=30,label="تکرار گذرواژه", widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    class Meta:
        model = User
        fields = ['username', 'email']

    def clean(self):
        """
        validates passwords matching and if it is good with Django validations.
        :return:
        """
        data = super().clean()
        p1 = data.get('p1')
        p2 = data.get('p2')
        if p1 != p2:
            raise ValidationError('گذروازه ها با هم تطابق ندارد.')

        validate_password(p1)

    def save(self, commit=True):
        """
        we need to add our password in save so we customize our save abit.
        :param commit:
        :return:
        """
        user = super().save(commit=False)
        user.set_password(self.cleaned_data.get('p1'))
        user.save()
        return user

# #second way of register form using UserCreationForm
# class RegisterForm(UserCreationForm):
#     class Meta:
#         model = User
#         fields = ['username', 'email', 'password1', 'password2']

class LoginForm(forms.Form):
    username = forms.CharField(max_length=40, label='نام کاربری', widget=forms.Textarea(attrs={'class': 'form-control','rows': 1}))
    password = forms.CharField(max_length=40,label='رمز عبور', widget=forms.PasswordInput(attrs={'class': 'form-control'}))




# #second way of LoginForm using AuthenticationForm
# class LoginForm(AuthenticationForm):
#     class Meta:
#         model = User
#         fields = ['username', 'password']




# ========================================================== OLD CODES ==================================================================

# class NewUser(forms.Form): #This was our previous way of making a new user,before we use Django inbuild ones. we got a better one now.
#     username = forms.CharField(label="نام کاربری", max_length=32)
#     password = forms.CharField(label="رمز عبور", max_length=20, widget=forms.PasswordInput(render_value=False))
#     # password = forms.CharField(label="رمز عبور", max_length=20, widget=forms.PasswordInput(render_value=False,attrs={'class':'bnazanin'})) why not working for label???
#     birthdate = forms.DateField(label="تاریخ تولد",
#                                 widget=forms.DateInput(attrs={'type': 'date', 'class': 'datepicker'}))
#     bio = forms.CharField(label='درباره من', widget=forms.Textarea(attrs={'class': 'form-control'}))
#     gender = forms.CharField(label='جنسیت', choices=GenderChoices.choices)
#     city = forms.ChoiceField(label="شهر محل سکونت", choices=CityChoices.choices, initial=CityChoices.ISFAHAN)
#     email = forms.EmailField(label="ایمیل")
#     close_friend = forms.ModelMultipleChoiceField(label="دوستان نزدیک", queryset=User.objects.all())
#
#     def clean_username(self):
#         """
#         this is to make sure username is not empty
#         :return: empty validation error
#
#         """
#         username = self.cleaned_data.get('username')
#         if len(username) == 0:
#             raise forms.ValidationError('این فیلد نمیتواند خالی باشد')
#         return username
#
#     def clean_password(self):
#         """
#         this is to make sure password is not empty
#         :return: empty validation error
#
#         """
#         password = self.cleaned_data.get('password')
#         if len(password) == 0:
#             raise forms.ValidationError('این فیلد نمیتواند خالی باشد')
#         return password
