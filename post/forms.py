from django import forms
from django.forms import TextInput, FileInput, Textarea

from post.models import Post, Comment


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['image', 'title', 'description']

    widgets = {
        'title': TextInput(attrs={'class': 'form-control',
                                  'placeholder': 'Enter the title'}),
        'description': Textarea(attrs={'class': 'form-control',
                                       'placeholder': 'Write here...'}),
        'image': FileInput(attrs={'class': 'form-control',
                                  'placeholder': 'Select an image to upload'})
    }


class PostUpdateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['image', 'title', 'description']

        widgets = {
            'image': FileInput(attrs={'class': 'form-control', 'placeholder': 'Select an image to upload'}),
            'title': TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter the title'}),
            'description': Textarea(attrs={'class': 'form-control', 'placeholder': 'Write here...'})
        }


class PostCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['body']

        widgets = {
            'name': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your name'
            }),
            'body': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your comment here'
            })
        }
