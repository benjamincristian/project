from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView

from post.forms import PostForm, PostUpdateForm, NewCommentForm
from post.models import Post, BlogComment


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


class PostDetailView(LoginRequiredMixin, DetailView):
    template_name = 'post/detail_post.html'
    model = Post

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)

        # we retrieve all the comments stored in the PostBlog object, then we store them in the variable below
        comments_connected = BlogComment.objects.filter(blogpost_connected=self.get_object())
        data['comments'] = comments_connected
        if self.request.user.is_authenticated:
            data['comment_form'] = NewCommentForm(instance=self.request.user)
        return data

    def post(self, request, *args, **kwargs):
        new_comment = BlogComment(content=request.POST.get('content'),
                                  author=self.request.user,
                                  blogpost_connected=self.get_object())
        new_comment.save()
        return self.get(self, request, *args, **kwargs)


@login_required
def like_view(request, pk):
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    post.likes.add(request.user)
    return HttpResponseRedirect(reverse('detail-blog', args=[str(pk)]))


@login_required
def dislike_view(request, pk):
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    post.dislikes.add(request.user)
    return HttpResponseRedirect(reverse('detail-blog', args=[str(pk)]))


@login_required()
def search_bar(request):
    get_value = request.GET.get('search')
    if get_value:
        posts = Post.objects.filter(Q(title__icontains=get_value))
    else:
        posts = {}

    return render(request, 'post/search.html', {'all_posts': posts})
