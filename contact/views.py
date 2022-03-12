from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from .models import Contact
from .forms import ContactForm

def contact(request):
    EMAIL_HOST_USER = settings.EMAIL_HOST_USER

    if request.method == "POST":
        form = ContactForm(request.POST, request.FILES)
        if form.is_valid():
            contact = form.save(commit=False)
            #form.save()
            name = request.POST.get('name')
            email = request.POST.get('email')
            subject = request.POST.get('subject')
            message = request.POST.get('message')
            send_mail(subject, message, email, EMAIL_HOST_USER, fail_silently = False)
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