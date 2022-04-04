""" Contact app Views """
from django.shortcuts import render
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from .forms import ContactForm


def contact(request):
    """ Contact form """
    if request.method == "POST":
        form = ContactForm(request.POST, request.FILES)
        if form.is_valid():
            contact = form.save(commit=False)
            name = request.POST.get('name')
            email = request.POST.get('email')
            subject = request.POST.get('subject')
            message = request.POST.get('message')

            send_mail(
                subject,
                message,
                settings.EMAIL_HOST_USER, [email], fail_silently=True
            )

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
