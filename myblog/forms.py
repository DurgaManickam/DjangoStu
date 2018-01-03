from django import forms
from .models import Post

class PostFormm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('author',)

class PostForm(forms.Form):
    author =  forms.CharField(max_length=20)

class TestForm(forms.Form):
    phoneNumber = forms.CharField(max_length=10)

class UserEntryForm(forms.Form):
    name = forms.CharField(max_length=25)

    def clean_name(self):
        name = self.cleaned_data['name']
        return '{} Driver'.format(name)
