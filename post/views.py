from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView

from post.forms import PostForm, PostUpdateForm
from post.models import Post


# Create your views here.


class PostCreateView(CreateView):
    template_name = 'post/new_post_form.html'
    model = Post
    form_class = PostForm
    success_url = reverse_lazy('home')


class PostListView(ListView):
    template_name = 'post/list_of_post.html'
    model = Post
    context_object_name = 'all_posts'


class PostUpdateView(UpdateView):
    template_name = 'post/update_post.html'
    form_class = PostUpdateForm
    model = Post
    success_url = reverse_lazy('home')


class PostDeleteView(DeleteView):
    template_name = 'post/delete_post.html'
    model = Post
    success_url = reverse_lazy('home')

