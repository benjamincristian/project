from django.contrib.auth.models import User
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView

from userextend.forms import UserExtendForm


# Create your views here.

class UserExtendCreateView(CreateView):
    template_name = 'userextend/create_user.html'
    model = User
    form_class = UserExtendForm
    success_url = reverse_lazy('home')


class UserListView(ListView):
    template_name = 'userextend/list_user.html'
    model = User
    context_object_name = 'all_users'
