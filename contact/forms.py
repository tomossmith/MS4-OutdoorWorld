""" Contact App - forms.py """
from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):
    """
    Contact submit form
    """
    class Meta:
        """
        Contact form fields
        """
        model = Contact
        fields = '__all__'
