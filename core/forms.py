from django import forms
from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator
from unicodedata import category

from core.models import CategoryChoices, CityChoices, User, Post


# second way (Django form)
# class PostForm(forms.Form):
#     title = forms.CharField(label='تیتر', max_length=40,
#                             validators=[MinLengthValidator(3, 'این فیلد نمی تواند کمتر از 3 کاراکتر باشد')])
#     content = forms.CharField(label='شرح', max_length=255)
#     # userName = forms.CharField(label='نام کاربری', max_length=40)
#     userName = forms.ModelChoiceField(label='نام کاربری', queryset=User.objects.all(),
#                                       initial=User.objects.all().first())
#     visible = forms.BooleanField(label='نمایش')
#     category = forms.ChoiceField(label='موضوع', choices=CategoryChoices.choices)
#
#     def clean_content(self):
#         d = self.cleaned_data.get('content')
#         absurd_words = ['hello', 'hi', 'bye']
#         for word in absurd_words:
#             if word in d:
#                 raise forms.ValidationError('لحنتو بفهم')
#         return d

# third way(model form)
class PostForm(forms.ModelForm):
    # tag = forms.CharField(max_length=40, widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Post
        fields = ['title', 'content', 'user', 'category', 'show_to', 'visible']

        widgets = {
            "content": forms.Textarea(attrs={'class': 'form-control'}),
            "category": forms.RadioSelect(attrs={'class': 'form-radio'}),

        }
        # error_messages = {
        #     'title':{
        #         'required':'این فیلد اجباری است',
        #         'max-length':'تعداد کاراکتر ها بیش از حد مجاز است'
        #     }
        # }

    def clean_content(self):
        content = self.cleaned_data.get('content')
        if len(content) < 3:
            raise forms.ValidationError("این فیلد نمیتماند کمتر از 3 کاراکتر باشد")
        return content

    def clean(self):
        data = super().clean()
        title = data.get('title')
        content = data.get('content')
        if title not in content:
            raise forms.ValidationError('تیتر حتما باید در متن پست باشد')


class NewUser(forms.Form):
    username = forms.CharField(label="نام کاربری", max_length=32)
    password = forms.CharField(label="رمز عبور", max_length=20, widget=forms.PasswordInput(render_value=False))
    # password = forms.CharField(label="رمز عبور", max_length=20, widget=forms.PasswordInput(render_value=False,attrs={'class':'bnazanin'})) why not working for label???
    birthdate = forms.DateField(label="تاریخ تولد",
                                widget=forms.DateInput(attrs={'type': 'date', 'class': 'datepicker'}))
    bio = forms.CharField(label='درباره من',widget=forms.Textarea(attrs={'class': 'form-control'}))
    city = forms.ChoiceField(label="شهر محل سکونت", choices=CityChoices.choices, initial=CityChoices.ISFAHAN)
    email = forms.EmailField(label="ایمیل")
    close_friend = forms.ModelMultipleChoiceField(label="دوستان نزدیک", queryset=User.objects.all())

    def clean_username(self):
        """
        this is to make sure username is not empty
        :return: empty validation error

        """
        username = self.cleaned_data.get('username')
        if len(username) == 0:
            raise forms.ValidationError('این فیلد نمیتواند خالی باشد')
        return username

    def clean_password(self):
        """
        this is to make sure password is not empty
        :return: empty validation error

        """
        password = self.cleaned_data.get('password')
        if len(password) == 0:
            raise forms.ValidationError('این فیلد نمیتواند خالی باشد')
        return password
