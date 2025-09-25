from django.urls import path
from .views import PostListCreateView

app_name = 'api_microblog'

urlpatterns = [
    path('posts/', PostListCreateView.as_view(), name='post-list-create'),
]
