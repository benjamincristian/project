from django import forms
from django.forms import TextInput, FileInput, Textarea

from post.models import Post, BlogComment


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


class NewCommentForm(forms.ModelForm):
    class Meta:
        model = BlogComment
        fields = ['content']

        widgets = {
            'content': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Leave a comment...'
            })
        }
