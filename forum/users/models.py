from django.db import models

# Create your models here.


class User(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    avatar = models.CharField(max_length=300)
    address = models.CharField(max_length=100)
