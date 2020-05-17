from rest_framework import viewsets
from .serializers import PostSerializer, UserSerializer, CategorySerializer
from .models import Post, Category
from django.contrib.auth.models import User
from rest_framework.response import Response
from django.db.models import Q


class PostViewSet(viewsets.ModelViewSet):
    serializer_class = PostSerializer

    def get_queryset(self):
        queryset = Post.objects.order_by('replies')
        title = self.request.query_params.get('title', None)
        if title is not None:
            queryset = queryset.filter(Q(title__contains=title))
        return queryset


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
