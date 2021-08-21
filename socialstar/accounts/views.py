from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import CreateView

from socialstar.accounts.forms import UserCreateForm


class RegisterView(CreateView):
    form_class = UserCreateForm
    success_url = reverse_lazy('login page')
    template_name = 'accounts/register.html'
