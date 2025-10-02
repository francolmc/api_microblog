from django.urls import path
from .views import PostListCreateView, PostDetailView

app_name = 'api_microblog'

urlpatterns = [
    path('posts/', PostListCreateView.as_view(), name='post-list-create'),
    path('posts/<int:pk>/', PostDetailView.as_view(), name='post-detail')
]
