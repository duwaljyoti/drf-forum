from rest_framework import viewsets, views
from .serializers import PostSerializer, UserSerializer, CategorySerializer
from .models import Post, Category, Reply
from django.contrib.auth.models import User
from rest_framework.response import Response
from django.db.models import Q
from rest_framework.decorators import api_view
from django.db.models import Subquery, Count
from django.core.signals import request_finished
from django.dispatch import receiver, Signal
import time


# @receiver(request_finished, sender=Post, dispatch_uid='something')
def test_listener(sender, **test_kwargs):
    time.sleep(4)
    print('Request Finished')


request_finished.connect(test_listener)
# Signal.connect(test_listener, sender=None)


class PostViewSet(viewsets.ModelViewSet):
    serializer_class = PostSerializer
    queryset = Post.objects

    def get_queryset(self):
        # queryset = Post.objects.order_by('replies')
        queryset = Post.objects.annotate(reply_count=Count('replies')).order_by('-reply_count')
        string_query = str(queryset.query)
        test_list = list(queryset.all())
        title = self.request.query_params.get('title', None)
        if title is not None:
            # queryset = queryset.filter(Q(title__contains=title) | Q(description__contains=title))
            # queryset = queryset.filter(Q(title__contains=title) & Q(description__contains=title))
            queryset = queryset.filter(Q(title__contains=title))
                # .values('title')
            # first = queryset = queryset.filter(~Q(title__contains='first'))
            # second = queryset = queryset.filter(~Q(title__contains='second'))
            # queryset = first.union(second)

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


class ClassBasedView(views.APIView):
    def get(self, request, format=None):
        return Response('something')


@api_view(['GET'])
def function_based_view(request):
    return Response('An example of function based view.')


@api_view(['GET'])
def post_with_replies(request):
    replies = Reply.objects.all()
    posts_with_replies = Post.objects.filter(replies__in=Subquery(replies.values('id')))

    # user_count = User.objects.filter(active=True).count()
    # content = {'user_count': user_count}
    data = {'data': posts_with_replies}
    # object of type post is not serializable
    return Response(data)
    # return Response({'key': 'value'}, status=status.HTTP_200_OK)
    # return Response({'data': posts_with_replies}, status=200)


@api_view(['GET'])
def post_with_replies_using_join(request):
    posts = Post.objects.select_related('user')
    # Article.objects.select_related('reporter')

    # https: // books.agiliq.com / projects / django - orm - cookbook / en / latest / join.html

    return Response(data=posts)
