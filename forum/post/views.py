from rest_framework import viewsets
from .serializers import PostSerializer, UserSerializer, CategorySerializer
from .models import Post, Category
from django.contrib.auth.models import User
from rest_framework.response import Response


class PostViewSet(viewsets.ModelViewSet):
    serializer_class = PostSerializer
    queryset = Post.objects.all().order_by('-id')


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()


class CategoryViewSet(viewsets.ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()

    def list(self, request, *args, **kwargs):
        queryset = Category.objects.all()
        serializer = CategorySerializer(queryset, many=True)

        return Response(data=serializer.data)
