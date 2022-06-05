from django import forms
from .models import post
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Field


class postForm(forms.ModelForm):
    class Meta:
        model = post
        fields = ('image', 'caption')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            'image',
            'caption',
            Submit('submit', 'Post', css_class='btn-primary')
        )