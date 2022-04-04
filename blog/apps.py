""" Blog App Config """
from django.apps import AppConfig


class BlogConfig(AppConfig):
    """ Configuration for the Blog App """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'blog'
