from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    title = models.CharField(max_length=300)


class Post(models.Model):
    user = models.ForeignKey(User, related_name='posts', on_delete=models.CASCADE)
    title = models.CharField(max_length=300)
    description = models.CharField(max_length=300)
    view_counter = models.CharField(max_length=300)
    categories = models.ManyToManyField(Category, related_name='posts')

    # def __str__(self):
    #     return self.product.name


class Reply(models.Model):
    comment = models.TextField()
    user = models.ForeignKey(User, related_name='replies', on_delete=models.CASCADE)
    post = models.ForeignKey(Post, related_name='replies', on_delete=models.CASCADE)
    is_best = models.BooleanField()
