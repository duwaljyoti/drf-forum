from rest_framework import viewsets
from .serializers import PostSerializer, UserSerializer
from .models import Post
from django.contrib.auth.models import User


class PostViewSet(viewsets.ModelViewSet):
    serializer_class = PostSerializer
    queryset = Post.objects.all().order_by('-id')


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
