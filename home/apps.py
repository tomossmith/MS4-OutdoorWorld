""" Homepage - apps.py """
from django.apps import AppConfig


class HomeConfig(AppConfig):
    """
    Homepage configuration
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'home'
