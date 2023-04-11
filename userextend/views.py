from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView, DeleteView, UpdateView
from userextend.forms import UserExtendForm
from django.http import HttpResponseForbidden


class UserExtendCreateView(CreateView):
    template_name = 'userextend/create_user.html'
    model = User
    form_class = UserExtendForm
    success_url = reverse_lazy('home')


class UserListView(LoginRequiredMixin, ListView):
    template_name = 'userextend/list_user.html'
    model = User
    context_object_name = 'all_users'


class UserDetailView(LoginRequiredMixin, DetailView):
    template_name = 'userextend/detail_user.html'
    model = User

    def get_queryset(self):
        return User.objects.filter(pk=self.request.user.pk)

    def dispatch(self, request, *args, **kwargs):
        user = self.get_object()
        if user != request.user:
            return HttpResponseForbidden("You are not allowed to edit this profile.")
        return super().dispatch(request, *args, **kwargs)


class UserDeleteView(LoginRequiredMixin, DeleteView):
    template_name = 'userextend/delete_user.html'
    model = User
    success_url = reverse_lazy('home')


class UserUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'userextend/update_user.html'
    model = User
    form_class = ''
    success_url = reverse_lazy('detail-user')
