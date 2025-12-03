from django import forms
from django.core.validators import MaxLengthValidator, MinLengthValidator

from core.models import CategoryChoices


class PostForm(forms.Form):
    title=forms.CharField(label='تیتر',max_length=40,validators=[MinLengthValidator(3,'این فیلد نمی تواند کمتر از 3 کاراکتر باشد')])
    content=forms.CharField(label='شرح',max_length=255)
    userName=forms.CharField(label='نام کاربری',max_length=40)
    visible=forms.BooleanField(label='نمایش')
    category=forms.ChoiceField(label='موضوع',choices=CategoryChoices.choices)

    def clean_content(self):
        d=self.cleaned_data.get('content')
        absurd_words=['hello','hi','bye']
        for word in absurd_words:
            if word in d:
                raise forms.ValidationError('لحنتو بفهم')
        return d
