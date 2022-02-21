from django import forms
from .models import Post
from .widgets import CustomClearableFileInput


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        exclude = ('author',)
        fields = ('title', 'content', 'image',)

    image = forms.ImageField(label='Image', required=False, widget=CustomClearableFileInput)

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'title': 'Title',
            'content': 'Content',
            'image': 'Image',
        }
    

