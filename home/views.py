from django.shortcuts import render, redirect, reverse, get_object_or_404, HttpResponse
from django.contrib import messages
from django.conf import settings


# Create your views here.

def index(request):
    """ A view to return the index page """
    
    return render(request, 'home/index.html')

def contact(request):
    """ A view to return the index page """

    if request.method == 'POST':
        messages.error(request, 'Thank you for contacting us, we aim to respond within \
            2 working days.')
        return render(request, 'home/contact.html')         
    
    return render(request, 'home/contact.html')
