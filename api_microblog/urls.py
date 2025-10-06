from django.urls import path
from .views import PostListCreateView, PostDetailView, RegisterView, TokenObtainPairView

app_name = 'api_microblog'

urlpatterns = [
    path('posts/', PostListCreateView.as_view(), name='post-list-create'),
    path('posts/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('register/', RegisterView.as_view(), name='register'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
]
