""" Contact App - views.py """
from django.shortcuts import render
from django.contrib import messages
from django.core.mail import EmailMessage
from .forms import ContactForm


def contact(request):
    """
    Contact form
    """
    if request.method == "POST":
        form = ContactForm(request.POST, request.FILES)
        if form.is_valid():
            from_email = request.POST.get('email')
            subject = request.POST.get('subject')
            message = request.POST.get('message')

            email = EmailMessage(
                subject=subject,
                body=message,
                from_email=from_email,
                to=['outdoorworldms4@gmail.com'],
                reply_to=[from_email],
            )

            email.send()

            messages.success(
                request, 'Successfully sent message, a member of \
                    our team will reply as soon as possible.')

            template = 'home/index.html'
            return render(request, template)
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
