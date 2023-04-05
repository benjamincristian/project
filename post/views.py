from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView
from post.forms import PostForm, PostUpdateForm, NewCommentForm
from post.models import Post, PostComment


class PostCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    template_name = 'post/new_post_form.html'
    model = Post
    form_class = PostForm
    success_url = reverse_lazy('view-blog')
    permission_required = 'post.add_post'


class PostListView(LoginRequiredMixin, ListView):
    template_name = 'post/list_of_post.html'
    model = Post
    context_object_name = 'all_posts'


class PostUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    template_name = 'post/update_post.html'
    form_class = PostUpdateForm
    model = Post
    success_url = reverse_lazy('view-blog')
    permission_required = 'post.change_post'


class PostDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    template_name = 'post/delete_post.html'
    model = Post
    success_url = reverse_lazy('view-blog')
    permission_required = 'post.delete_post'


class PostDetailView(LoginRequiredMixin, DetailView):
    template_name = 'post/detail_post.html'
    model = Post

    def get_context_data(self, **kwargs):
        # This variable 'data' collects all the data related to one post
        data = super().get_context_data(**kwargs)

        # we retrieve all the comments related to one post
        comments_connected = PostComment.objects.filter(blogpost_connected=self.get_object())

        # all the comments are stored in this variable below
        data['comments'] = comments_connected
        if self.request.user.is_authenticated:
            data['comment_form'] = NewCommentForm(instance=self.request.user)
        return data

    def post(self, request, *args, **kwargs):  # the request parameter, is a HTTP request
        # the variable below creates a new comment with the following parameters: content, author and blogpost_connected
        # which is the post itself
        new_comment = PostComment(content=request.POST.get('content'),
                                  author=self.request.user,
                                  blogpost_connected=self.get_object())
        new_comment.save()  # with this the comment is saved
        return self.get(self, request, *args, **kwargs)  # this is going to refresh the page with the new comment added


@login_required
def like_view(request, pk):
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    post.likes.add(request.user)
    return HttpResponseRedirect(reverse('detail-blog', args=[str(pk)]))


@login_required
def comment_like_view(request, pk):
    comment = get_object_or_404(PostComment, id=request.POST.get('comment_id'))
    comment.likes.add(request.user)
    return HttpResponseRedirect(reverse('comment', args=[str(pk)]))


@login_required
def dislike_view(request, pk):
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    post.dislikes.add(request.user)
    return HttpResponseRedirect(reverse('detail-blog', args=[str(pk)]))


@login_required()
def search_bar(request):
    get_value = request.GET.get('search')
    if get_value:
        posts = Post.objects.filter(Q(title__icontains=get_value) | Q(small_description__icontains=get_value))
    else:
        posts = {}

    return render(request, 'post/search.html', {'all_posts': posts})


@login_required()
def activate_deactivate_post(request, pk):
    Post.objects.filter(id=pk).update(active=False)
    return redirect('view-blog')
