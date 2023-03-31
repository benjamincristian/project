from django import forms
from django.forms import TextInput, FileInput, Textarea
from post.models import Post, PostComment


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
        fields = ['description', 'image', 'title', 'small_description']

        widgets = {
            'description': Textarea(attrs={'class': 'form-control', 'placeholder': 'Write here...'}),
            'image': FileInput(attrs={'class': 'form-control', 'placeholder': 'Select an image to upload'}),
            'title': TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter the title'}),
            'small_description': TextInput(attrs={'class': 'form-control', 'placeholder': 'Write here...'})
        }


class NewCommentForm(forms.ModelForm):
    class Meta:
        model = PostComment
        fields = ['content']

        widgets = {
            'content': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Write your comment here...'
            })
        }
