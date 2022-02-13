from django.shortcuts import render

# Create your views here.

def index(request):
    """ A view to return the index page """
    
    return render(request, 'home/index.html')

def contact(request):
    """ A view to display a contact form """

    return render(request, 'home/contact.html')