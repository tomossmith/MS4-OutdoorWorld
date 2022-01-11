from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        message.error(request, "There's nothing in your bag at the moment")
        return redirect (reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51KGpBDCtnAJ7AfbFzi9bDp8QG9iK8mVbrAMH54qr6NPLxSVflbnQ9g1IJ4wwvey36eAzmgik1z1jmYu9Z45qjmPe005kG37h13',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)