from django import forms
from django.forms import TextInput, FileInput, Textarea
from post.models import Post, PostComment


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['image', 'title', 'tags', 'description', 'small_description']

        widgets = {
            'title': TextInput(attrs={'class': 'form-control',
                                      'placeholder': 'This is going to appear on the page with all the posts'}),
            'description': Textarea(attrs={'class': 'form-control',
                                           'placeholder': 'Write here...'}),
            'small_description': TextInput(attrs={'class': 'form-control',
                                                  'placeholder': 'This is going to appear on the page with '
                                                                 'all the posts'}),
            'image': FileInput(attrs={'class': 'form-control',
                                      'placeholder': 'Select an image to upload'}),
            'tags': TextInput(attrs={'class': 'form-control',
                                     'placeholder': 'Enter the tags related to this post...'})
        }


class PostUpdateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['description', 'image', 'title', 'small_description', 'tags']

        widgets = {
            'description': Textarea(attrs={'class': 'form-control', 'placeholder': 'Write here...'}),
            'image': FileInput(attrs={'class': 'form-control', 'placeholder': 'Select an image to upload'}),
            'title': TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter the title'}),
            'small_description': TextInput(attrs={'class': 'form-control', 'placeholder': 'Write here...'}),
            'tags': TextInput(attrs={'class': 'form-control', 'placeholder': 'Add tags here...'})
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
