from django.shortcuts import render
from django.conf import settings
from .models import Post
from django.views import generic


#def blog(request):
    #return render(request, 'blog/blog.html')

class postlist(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('created_on')
    template_name = 'blog/blog.html'