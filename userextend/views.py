from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView, DeleteView, UpdateView
from userextend.forms import UserExtendForm


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


class UserDeleteView(LoginRequiredMixin, DeleteView):
    template_name = 'userextend/delete_user.html'
    model = User
    success_url = reverse_lazy('home')


class UserUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'userextend/update_user.html'
    model = User
    form_class = ''
    success_url = reverse_lazy('detail-user')
