""" Products App - models.py """
from django.db import models


class Category(models.Model):
    """
    Product Category Models
    """
    class Meta:
        """
        Categories Fields
        """
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        """
        Product Friendly Names
        """
        return self.friendly_name


SIZE_CHOICES = [
    ('clothing', 'Clothing'),
    ('footwear', 'Footwear'),
    ('no-sizes', 'No Sizing'),
]


class Product(models.Model):
    """
    Product Fields
    """
    category = models.ForeignKey(
        'Category', null=True, blank=True, on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254, null=True, blank=True)
    brand = models.CharField(max_length=254)
    name = models.CharField(max_length=254)
    description = models.TextField()
    has_sizes = models.CharField(
        max_length=15, choices=SIZE_CHOICES, default='no-sizing')
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name
