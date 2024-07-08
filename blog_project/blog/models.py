from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth.models import User


class Post(models.Model):
    """
    A class to represent a blog post.
    """
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'"{self.title}" by {self.author}'
    
    def get_absolute_url(self):
        return reverse('blog-post-detail', kwargs={'pk': self.pk, })


class Comment(models.Model):
    """
    A class to represent a comments on a blog post.
    """
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'"On {self.post.title}" by {self.author}'
