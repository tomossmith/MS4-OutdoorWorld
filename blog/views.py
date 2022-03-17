from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Count

from .models import Post, Comment
from .forms import CommentForm, PostForm

""" A view to show all the blog posts. """
def blog(request):
    posts = Post.objects.all()

    return render(request, 'blog/blog.html', {'posts': posts})


""" A view to show more of a selected blog post """
def post_detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    template = 'blog/post_detail.html'
    form = CommentForm()
    comment_count= Comment.objects.all().count()
    
    context = {
        'post': post,
        'form': form,
        'comment_count': comment_count
    }

    if request.method == 'POST':
        form = CommentForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()

            return redirect(reverse('post_detail', args=[post.id]))

    return render(request, template, context)


""" A view to to allow an admin to add a blog post """
@login_required
def add_post(request):
    if not request.user.is_superuser:
        messages.error(request,
                       'Sorry, only administrators can add a blog post')
        return redirect(reverse('blog'))

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save()
            form.save()
            messages.success(request, 'Successfully added Blog Post!')
            return redirect(reverse('post_detail', args=[post.id]))
        else:
            messages.error(request,
                           'Could not add post to site. \
                           Please ensure form is valid!')
    else:
        form = PostForm()

    template = 'blog/add_post.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


""" A view to to allow an admin to edit a blog post """
@login_required
def edit_post(request, post_id):
    if not request.user.is_superuser:
        messages.error(request,
                       'Sorry, only the admin can edit a blog post')
        return redirect(reverse('blog'))

    post = get_object_or_404(Post, pk=post_id)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            data = form.save(commit=False)
            data.user = request.user
            form.save()
            messages.success(request, 'Successfully Updated Blog Post!')
            return redirect(reverse('post_detail', args=[post.id]))
        else:
            messages.error(request,
                           'Could not add post to site. \
                           Please ensure form is valid!')
    else:
        form = PostForm(instance=post)
        messages.info(request, f'You are editing a post titled: {post.title}')

    template = 'blog/edit_post.html'
    context = {
        'form': form,
        'post': post,
    }

    return render(request, template, context)

""" A view to to allow an admin to delete a blog post """
@login_required
def delete_post(request, post_id):
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only the administrator can remove a blog post.')
        return redirect(reverse('blog'))

    selected_post = get_object_or_404(Post, pk=post_id)
    selected_post.delete()
    messages.success(request, 'The Post has been deleted!')

    return redirect(reverse('blog'))

""" A view to to allow an admin to delete a comment on a post """
@login_required
def delete_comment(request, comment_id):
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only the administrator can remove a comment from a post!')
        return redirect(reverse('blog'))

    else:
        comment = get_object_or_404(Comment, pk=comment_id)
        comment.delete()
        messages.success(request, 'The comment was succesfully deleted!')

        return redirect(reverse('blog'))