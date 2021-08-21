from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db import IntegrityError
from django.shortcuts import get_object_or_404
# Create your views here.
from django.urls import reverse
from django.views.generic import CreateView, DetailView, ListView, RedirectView

from socialstar.groups.models import Group, GroupMember


class CreateGroup(LoginRequiredMixin, CreateView):
    fields = ('name', 'description')
    model = Group


class SingleGroup(DetailView):
    model = Group


class ListGroup(ListView):
    model = Group


class JoinGroup(LoginRequiredMixin, RedirectView):

    def get_redirect_url(self, *args, **kwargs):
        return reverse('groups:single', kwargs={'slug': self.kwargs.get('slug')})

    def get(self, request, *args, **kwargs):
        group = get_object_or_404(Group, slug=self.kwargs.get('slug'))

        try:
            GroupMember.objects.create(user=self.request.user, group=group)
        except IntegrityError:
            messages.warning(self.request, ('Warning already a member!'))
        else:
            messages.success(self.request, 'You are now a member')
        return super().get(request, *args, **kwargs)


class LeaveGroup(LoginRequiredMixin, RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        return reverse('groups:single', kwargs={'slug': self.kwargs.get('slug')})

    def get(self, request, *args, **kwargs):
        group = get_object_or_404(Group, slug=self.kwargs.get('slug'))

        try:
            membership = GroupMember.objects.filter(user=self.request.user,
                                                    group__slug=self.kwargs.get('slug')).get()
        except GroupMember.DoesNotExist:
            messages.warning(self.request, 'Sorry you are not a member of this group')
        else:
            membership.delete()
            messages.success(self.request,'You have left the group!')
        return super().get(request, *args, **kwargs)

