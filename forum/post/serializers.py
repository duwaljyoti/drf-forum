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
        fields = ('comment', 'user_id', 'user', 'is_best')


class PostsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('id', 'title', 'description')


class CategorySerializer(serializers.ModelSerializer):
    posts = PostsSerializer(many=True)

    class Meta:
        model = Category
        fields = ('id', 'title', 'posts')


class PostSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.first_name')
    categories = CategorySerializer(many=True, read_only=True)
    replies = ReplySerializer(many=True)

    # count_replies = serializers.SerializerMethodField()

    def get_count_replies(self, post_object):
        return post_object.replies.count()

    class Meta:
        model = Post
        fields = (
            'id',
            'title',
            # 'description',
            'user',
            'categories',
            'replies',
            # 'count_replies'
        )
        # ordering = ['count_replies', 'asc']
