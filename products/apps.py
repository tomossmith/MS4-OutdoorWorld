""" Products App - apps.py """
from django.apps import AppConfig


class ProductsConfig(AppConfig):
    """
    product configuration
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'products'
