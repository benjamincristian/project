from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from post.forms import PostForm
from post.models import Post


# Create your views here.


class PostCreateView(CreateView):
    template_name = 'post/new_post_form.html'
    model = Post
    form_class = PostForm
    success_url = reverse_lazy('home')


