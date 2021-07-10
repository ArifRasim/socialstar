from django.urls import path

from socialstar.posts.views import PostList, CreatePost, UserPosts, PostDetail, DeletePost

app_name = 'posts'

urlpatterns = [
    path('', PostList.as_view(), name='all'),
    path('new/', CreatePost.as_view(), name='create'),
    path('by/<slug:username>/', UserPosts.as_view(), name='for_user'),
    path('details/<slug:username>/<int:pk>/', PostDetail.as_view(), name='single'),
    path('delete/<int:pk>/', DeletePost.as_view(), name='delete'),
]
