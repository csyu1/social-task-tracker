from __future__ import absolute_import, unicode_literals

from django.conf.urls import url

from . import views

urlpatterns = [
    url(
        regex=r'groups/$',
        view=views.GroupListView.as_view(),
        name='group-list'
    ),
    url(
        regex=r'create-group/$',
        view=views.GroupCreateView.as_view(),
        name='group-create'
    ),
    url(
        regex=r'^groups/(?P<pk>[0-9]+)/$',
        view=views.GroupDetailView.as_view(),
        name='group-detail'
    ),

]
