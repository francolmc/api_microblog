from rest_framework import generics, status
from .models import Post
from .serializers import PostSerializer
from .pagination import CustomPagination
from django_filters.rest_framework import DjangoFilterBackend
from .filters import PostFilter
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView

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

class RegisterView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        if not username or not password:
            return Response({ "error": "Both username and password are required" }, status=status.HTTP_400_BAD_REQUEST)
        if User.objects.filter(username=username).exists():
            return Response({ "error": "Username is already taken" }, status=status.HTTP_400_BAD_REQUEST)
        
        # Registrar el usuario
        user = User.objects.create_user(username=username, password=password)
        refresh = RefreshToken.for_user(user)
        access_token = str(refresh.access_token)

        return Response({ "access_token": access_token, "refresh_token": str(refresh) }, status=status.HTTP_201_CREATED)
    
class TokenObtainPairView(TokenObtainPairView):
    pass