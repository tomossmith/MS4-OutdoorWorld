from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings


def index(request):
    """ A view to return the index page """

    return render(request, 'home/index.html')