from django import forms
from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator
from core.models import CategoryChoices, Post


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


class PostForm(forms.ModelForm): # third way(model form)
    # tag = forms.CharField(max_length=40, widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Post
        fields = ['title', 'content','image', 'user', 'category', 'show_to', 'visible']

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


class EditPostForm(forms.ModelForm):
    # user_display = forms.CharField(label="نویسنده",required=False,disabled=True) #first way of doing adding a just for show user value in our form.
    class Meta:
        model = Post
        # fields = ['title', 'user_display', 'content','image', 'category', 'show_to', 'visible'] #first way of doing adding a just for show user value in our form.
        fields = ['title', 'user', 'content','image', 'category', 'show_to', 'visible'] #second way of doing adding a just for show user value in our form.

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # # first way of adding a just for show user value in our form
        # if self.instance.pk:
        #     self.fields['user_display'].initial = self.instance.user.username

        #second way of doing adding a just for show user value in our form:
        self.fields['user'].disabled = True
    #second way of doing adding a just for show user value in our form
    def clean_user(self):
        '''
        since the user form is disabled, we use this validation to return post's actual user value to our form
        :return:
        '''
        return self.instance.user
