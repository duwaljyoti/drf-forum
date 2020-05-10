from rest_framework import serializers
from .models import Post, Reply, Category
from user.serializers import UserSerializer


# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ('id', 'username', 'posts', 'first_name', 'last_name')


class ReplySerializer(serializers.ModelSerializer):
    user = UserSerializer(many=False)

    class Meta:
        model = Reply
        fields = ('comment', 'user_id', 'user')


class CategorySerializer(serializers.ModelSerializer):
    # posts = serializers.PrimaryKeyRelatedField(queryset=Post.objects.all(), many=True)

    class Meta:
        model = Category
        fields = ('id', 'title')


class PostSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.first_name')
    categories = CategorySerializer(many=True, read_only=True)
    replies = ReplySerializer(many=True)

    class Meta:
        model = Post
        fields = ('id', 'title', 'description', 'user', 'replies', 'categories')
        ordering = ['id']
        # fields = '__all__'

    def __str__(self):
        return self.title

