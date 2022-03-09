from django import forms
from .models import Post
from .widgets import CustomClearableFileInput


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'content', 'image', 'author',)
        widgets = {'author': forms.HiddenInput(),}

    image = forms.ImageField(label='Image', required=False, widget=CustomClearableFileInput)

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'author': 'author',
            'title': 'Title',
            'content': 'Content',
            'image': 'Image',
        }
    

