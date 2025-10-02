from rest_framework import generics
from .models import Post
from .serializers import PostSerializer
from .pagination import CustomPagination
from django_filters.rest_framework import DjangoFilterBackend
from .filters import PostFilter

# Create your views here.
class PostListCreateView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    pagination_class = CustomPagination
    filter_backends = [DjangoFilterBackend]
    filterset_class = PostFilter

class PostDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer