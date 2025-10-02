from rest_framework import generics
from .models import Post
from .serializers import PostSerializer
from .pagination import CustomPagination

# Create your views here.
class PostListCreateView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    pagination_class = CustomPagination
    
class PostDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer