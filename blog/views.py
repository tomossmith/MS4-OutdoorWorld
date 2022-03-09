from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.core.paginator import Paginator


from .models import Post
from .forms import PostForm
    
""" A view to show all the blog posts """
def blog(request):
    
    posts = Post.objects.all().order_by('created_on')

    context = {
        'posts': posts,
    }

    return render(request, 'blog/blog.html', context)


@login_required
def add_post(request):
    """ Adds a blog post to the store """
    if not request.user.is_authenticated:
        messages.error(request,
                       'Sorry, you have to be logged in to post to the blog.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            form.save()
            messages.success(request, 'Successfully added Blog Post!')
            return redirect(reverse('blog'))
        else:
            messages.error(request,
                           'Could not add post to site. \
                           Please ensure form is valid!')
    else:
        form = PostForm()

    context = {
        'form': form,
    }

    return render(request, 'blog/add_post.html', context)


""" A view to display an expanded view of the chosen post """
def post_detail(request, post_id):
    
    post = get_object_or_404(Post, pk=post_id)
    request_user = request.user

    context = {
        'post': post,
        "request_user": request_user,
    }

    return render(request, 'blog/post_detail.html', context)