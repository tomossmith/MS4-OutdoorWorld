""" Views for the blog app """
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import Post, Comment
from .forms import CommentForm, PostForm


def blog(request):
    """ A view to show all the blog posts. """
    posts = Post.objects.all()

    return render(request, 'blog/blog.html', {'posts': posts})


def post_detail(request, post_id):
    """ A view to show more of a selected blog post """
    template_name = 'blog/post_detail.html'
    post = get_object_or_404(Post, pk=post_id)
    comments = post.comments.filter(active=True)
    comment_count = post.comments.filter(active=True).count()
    new_comment = None
    # Comment posted
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():

            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.post = post
            # Save the comment to the database
            new_comment.save()
    else:
        comment_form = CommentForm()

    context = {
        'post': post,
        'comments': comments,
        'new_comment': new_comment,
        'comment_form': comment_form,
        'on_blog_page': True,
        'comment_count': comment_count
    }

    return render(request, template_name, context)


@login_required
def add_post(request):
    """ A view to to allow an admin to add a blog post """
    if not request.user.is_superuser:
        messages.error(
            request, 'Sorry, only administrators can add a blog post')
        return redirect(reverse('blog'))

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save()
            form.save()
            messages.info(request, 'Successfully added Blog Post!')
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
        'on_blog_page': True
    }

    return render(request, template, context)


@login_required
def edit_post(request, post_id):
    """ A view to to allow an admin to edit a blog post """
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
        'on_blog_page': True
    }

    return render(request, template, context)


@login_required
def delete_post(request, post_id):
    """ A view to to allow an admin to delete a blog post """
    if not request.user.is_superuser:
        messages.error(
            request, 'Sorry, only the administrator can remove a blog post.')
        return redirect(reverse('blog'))

    selected_post = get_object_or_404(Post, pk=post_id)
    selected_post.delete()
    messages.info(request, 'The Post has been deleted!')

    return redirect(reverse('blog'))


@login_required
def delete_comment(request, comment_id):
    """ A view to to allow an admin to delete a comment on a post """
    if not request.user.is_superuser:
        messages.error(
            request, 'Sorry, only the administrator \
            can remove a comment from a post!')
        return redirect(reverse('blog'))

    else:
        comment = get_object_or_404(Comment, pk=comment_id)
        comment.delete()
        messages.info(request, 'The comment was succesfully deleted!')

        return redirect(reverse('blog'))
