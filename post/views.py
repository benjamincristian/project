from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView

from post.forms import PostForm, PostUpdateForm
from post.models import Post


# Create your views here.


class PostCreateView(LoginRequiredMixin, CreateView):
    template_name = 'post/new_post_form.html'
    model = Post
    form_class = PostForm
    success_url = reverse_lazy('view-blog')


class PostListView(LoginRequiredMixin, ListView):
    template_name = 'post/list_of_post.html'
    model = Post
    context_object_name = 'all_posts'


class PostUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'post/update_post.html'
    form_class = PostUpdateForm
    model = Post
    success_url = reverse_lazy('view-blog')


class PostDeleteView(LoginRequiredMixin, DeleteView):
    template_name = 'post/delete_post.html'
    model = Post
    success_url = reverse_lazy('view-blog')


class PostDetailView(DetailView):
    template_name = 'post/detail_post.html'
    model = Post


