
from django.utils import timezone
from django.contrib.auth.models import User
from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=600)
    text = models.CharField(max_length=255)

    like = models.ManyToManyField(User, blank=True, through='PostLike')


class PostLike(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    like_date = models.DateField(default=timezone.now)

