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
    request_user = request.user

    context = {
        'posts': posts,
        'search_term': query,
        "request_user": request_user,
        #'current_categories': categories,
        #'current_sorting': current_sorting,
    }

    return render(request, 'blog/all_posts.html', context)


""" A view to display an expanded view of the chosen post """
def post_detail(request, post_id):
    
    post = get_object_or_404(Post, pk=post_id)
    request_user = request.user

    context = {
        'post': post,
        "request_user": request_user,
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



""" A view to edit submitted posts """
@login_required
def edit_post(request, post_id):
    if not request.user.is_authenticated:
        messages.error(Request, 'Sorry, you must be logged in to edit posts')
        return redireect(reverse('blog'))

    post = get_object_or_404(Post, pk=post_id)
    request_user = request.user
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            message.success(request, 'Successfully updated the post!')
            return redirect(reverse('post_detail', args=[post_id]))
        else:
            messages.error(request, 'Failed to update the post, please ensure all fields are filled in correctly.')

    else:
        form = PostForm(instance=post)
        messages.info(request, f'You are editing {post.title}')

    template = 'blog/edit_post.html'
    context = {
        'form': form,
        'post': post,
        "request_user": request_user,
    }

    return render(request, template, context)