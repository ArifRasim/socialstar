from django.urls import path

from socialstar.groups.views import ListGroup, SingleGroup, CreateGroup, JoinGroup, LeaveGroup

app_name = 'groups'
urlpatterns = [
    path('', ListGroup.as_view(), name='all'),
    path('new/', CreateGroup.as_view(), name='create'),
    path('posts/<slug:slug>/', SingleGroup.as_view(), name='single'),
    path('join/<slug:slug>/', JoinGroup.as_view(), name='join'),
    path('leave/<slug:slug>/', LeaveGroup.as_view(), name='leave'),
]
