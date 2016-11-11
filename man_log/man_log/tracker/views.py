from __future__ import absolute_import, unicode_literals

from django.contrib.auth.models import Group
from django.core.urlresolvers import reverse
from django.views.generic.edit import CreateView
from django.views.generic import ListView
from django.views.generic import DetailView

from django.contrib.auth.mixins import LoginRequiredMixin


class GroupListView(LoginRequiredMixin, ListView):
    model = Group
    template_name = "tracker/group_list.html"


class GroupCreateView(LoginRequiredMixin, CreateView):
    model = Group
    fields = ['name']
    template_name = "tracker/group_form.html"

    def get_success_url(self):
        return reverse('tracker:group-list')


class GroupDetailView(LoginRequiredMixin, DetailView):
    model = Group
    template_name = "tracker/group_detail.html"
