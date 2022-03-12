from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from .models import Contact
from .forms import ContactForm


def contact(request):
    """ contact form """
    if request.method == "POST":
        EMAIL_HOST_USER = "outdoorworldms4@gmail.com"
        form = ContactForm(request.POST, request.FILES)
        if form.is_valid():
            contact = form.save(commit=False)
            # form.save()
            name = request.POST.get('name')
            email = request.POST.get('email')
            subject = request.POST.get('subject')
            message = request.POST.get('message')

            send_mail(
                subject,
                message,
                settings.EMAIL_HOST_USER, [email], fail_silently=True
            )

            messages.success(request, 'Successfully sent message')
            return render(request, 'contact/success.html')
        else:
            messages.error(request,
                           'Message could not be sent. \
                        Please ensure form is valid!')
    else:
        form = ContactForm()

    template = 'contact/contact.html'
    context = {
        'form': form,
    }

    return render(request, template, context)
