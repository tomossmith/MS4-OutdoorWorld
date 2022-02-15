from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings


def index(request):
    """ A view to return the index page """

    return render(request, 'home/index.html')

def contact(request):

    if request.method == 'POST':
        name = request.POST.get('name')
        message = request.POST.get('message')
        email = request.POST.get('email')
        send_mail(name, message, settings.EMAIL_HOST_USER,
                  [email], fail_silently=False)
        return render(request, 'home/email_success.html', {'email': email})

    return render(request, 'home/contact.html', {})