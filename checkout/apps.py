""" Checkout App - apps.py """
from django.apps import AppConfig


class CheckoutConfig(AppConfig):
    """
    Checkout config
    """
    name = 'checkout'

    def ready(self):
        import checkout.signals
