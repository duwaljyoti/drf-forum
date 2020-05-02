from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=300)
    description = models.CharField(max_length=300)
    view_counter = models.CharField(max_length=300)
