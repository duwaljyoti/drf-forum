from rest_framework import serializers
from .models import Post
from django.contrib.auth.models import User


class PostSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.first_name')

    class Meta:
        model = Post
        # fields = ('id', 'title', 'description','user')
        fields = '__all__'

    def __str__(self):
        return self.title


class UserSerializer(serializers.ModelSerializer):
    posts = PostSerializer(many=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'posts', 'first_name', 'last_name')
