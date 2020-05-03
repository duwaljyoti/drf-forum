from rest_framework import serializers
from django.contrib.auth.models import User
from post.models import Post
# try:
#     from post.serializers import PostSerializer
# except ImportError:
#     import sys
#     PostSerializer = sys.modules['__package__ ' + 'post.serializers.PostSerializer']


class PostSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.first_name')
    # replies = ReplySerializer(many=True)

    class Meta:
        model = Post
        fields = ('id', 'title', 'description', 'user', 'replies')
        ordering = ['id']
        # fields = '__all__'

    def __str__(self):
        return self.title


class UserSerializer(serializers.ModelSerializer):
    posts = PostSerializer(many=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'posts', 'first_name', 'last_name')
