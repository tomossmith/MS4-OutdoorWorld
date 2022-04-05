""" Contact App - models.py """
from django.db import models


class Contact(models.Model):
    """
    Contact models for the contact form
    """
    name = models.CharField(max_length=158)
    email = models.EmailField()
    subject = models.CharField(max_length=158)
    message = models.TextField()
