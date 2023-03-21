from django import forms
from django.forms import TextInput, FileInput, Textarea

from post.models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['image', 'title', 'description']
        exclude = ['likes', 'date']

    widgets = {
        'image': FileInput(attrs={'class': 'form-control',
                                  'placeholder': 'Select an image to upload'}),
        'title': TextInput(attrs={'class': 'form-control',
                                  'placeholder': 'Enter the title'}),
        'description': Textarea(attrs={'class': 'form-control',
                                       'placeholder': 'Write here...'})
    }