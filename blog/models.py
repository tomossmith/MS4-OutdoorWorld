from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date_added']

class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['date_added']