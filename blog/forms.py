""" Blog Forms """
from django import forms
from .widgets import CustomClearableFileInput
from .models import Post, Comment


class PostForm(forms.ModelForm):
    """ Post Form to render the fields in the form for the blog post. """
    class Meta:
        """ The fields to be used """
        model = Post
        fields = ['title', 'body', 'image_url']

    image = forms.ImageField(
        label='Image', required=False, widget=CustomClearableFileInput)


class CommentForm(forms.ModelForm):
    """ Comment Form to render the fields
    in the form for posting a comment. """
    class Meta:
        """ The fields to be used """
        model = Comment
        fields = ['name', 'email', 'body']
