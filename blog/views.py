from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.db.models.functions import Lower

from .models import Post
from .forms import PostForm


""" A view to show all the blog posts """
def all_posts(request):
    

    posts = Post.objects.all()
    query = None
    categories = None
    sort = None
    direction = None

    context = {
        'posts': posts,
        'search_term': query,
        #'current_categories': categories,
        #'current_sorting': current_sorting,
    }

    return render(request, 'blog/all_posts.html', context)


""" A view to display an expanded view of the chosen post """
def post_detail(request, post_id):
    
    post = get_object_or_404(Post, pk=post_id)

    context = {
        'post': post,
    }

    return render(request, 'blog/post_detail.html', context)


""" A view to add a post to the blog """
@login_required
def add_post(request):

    if not request.user.is_authenticated:
        messages.error(Request, 'Sorry, you must be logged in to add a post.')
        return redirect(reverse('blog'))

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save()
            messages.success(request, 'Product was successfully added to the store!')
            return redirect(reverse('post_detail', args=[post.id]))
        else:
            messages.error(request, 'failed to add post. Please ensure all fields in the form are filled correctly')
    else:
        form = PostForm()

    template = 'blog/add_post.html'
    context = {
        'form': form,
    }

    return render(request, template, context)
        