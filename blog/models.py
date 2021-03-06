""" Blog App - models.py """
from django.db import models


class Post(models.Model):
    """
    Create a blog post
    """
    title = models.CharField(max_length=255)
    body = models.TextField()
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        """
        set the order to display the post
        """
        ordering = ['-date_added']


class Comment(models.Model):
    """
    Submit a comment to a post
    """
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)

    class Meta:
        """
        Set the order in which comments should be displayed
        """
        ordering = ['date_added']

    def __str__(self):
        return 'Comment {} by {}'.format(self.body, self.name)
