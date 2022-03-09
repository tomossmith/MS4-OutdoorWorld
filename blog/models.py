from django.db import models
from django.contrib.auth.models import User

# https://djangocentral.com/building-a-blog-application-with-django/

STATUS = (
    (0,"Draft"),
    (1,"Publish")
)

class Post(models.Model):
    title = models.CharField(max_length=200, unique=False)
    author = models.ForeignKey(User, on_delete= models.CASCADE)
    updated_on = models.DateField(auto_now= True)
    content = models.TextField()
    created_on = models.DateField(auto_now_add=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return self.title