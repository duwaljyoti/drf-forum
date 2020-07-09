from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class UserParent(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    father_name = models.CharField(max_length=100)
    mother_name = models.CharField(max_length=100)
