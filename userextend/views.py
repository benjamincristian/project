from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView, DeleteView, UpdateView
from userextend.forms import UserExtendForm


class UserExtendCreateView(CreateView):
    template_name = 'userextend/create_user.html'
    model = User
    form_class = UserExtendForm
    success_url = reverse_lazy('home')


class UserListView(ListView):
    template_name = 'userextend/list_user.html'
    model = User
    context_object_name = 'all_users'


class UserDetailView(DetailView):
    template_name = 'userextend/detail_user.html'
    model = User


class UserDeleteView(DeleteView):
    template_name = 'userextend/delete_user.html'
    model = User
    success_url = reverse_lazy('home')


class UserUpdateView(UpdateView):
    template_name = 'userextend/update_user.html'
    model = User
    form_class = ''
    success_url = reverse_lazy('detail-user')
