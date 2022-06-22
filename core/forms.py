from django import forms
from . models import post
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Field


class postForm(forms.ModelForm):
    helper = FormHelper()
    helper.form_method = 'POST'
    helper.add_input(Submit('Post', 'Post', css_class='btn-primary'))
    class Meta:
        model = post
        fields = [
            'image', 
            'caption'
        ]

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model=User
        fields=['username','email','password1','password2']