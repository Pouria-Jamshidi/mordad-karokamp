from django import forms
from accounts.models import User

class RegisterForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']


















# class NewUser(forms.Form): #This was our previous way of making a new user. we got a better one now.
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
