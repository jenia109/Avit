from django.db import models
from django.utils import timezone

from myproject.core.models import CustomUser


class Post(models.Model):
    author = models.ForeignKey(CustomUser, related_name='posts', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='posts')
    date_pub = models.DateTimeField(default=timezone.now)
    date_edit = models.DateTimeField(default=timezone.now)
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=1000, blank=True)
    favorites = models.ManyToManyField(CustomUser, related_name='favorites_post', blank=True)

    def __str__(self):
        return f"Post from {self.author.username}"

    @property
    def get_favorites(self):
        return self.favorites.count()


class Comment(models.Model)
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    text = models.TextField(max_length=150)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    date_pub = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Comment from {self.author.username} to {post.title}"
