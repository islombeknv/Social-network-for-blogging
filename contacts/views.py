from django.contrib import messages
from django.core.mail import send_mail
from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic import CreateView
from blogs import settings
from contacts.forms import ContactModelForm


class ContactCreateView(CreateView):
    template_name = 'contact.html'
    form_class = ContactModelForm
    success_url = '/contact/done/'

    def form_valid(self, form):
        obj = form.save()
        text = f'Name: {obj.name}\nEmail: {obj.email}\nMessage: {obj.comment}\nDate{obj.created_at}'
        send_mail(
            'Notification',
            text,
            settings.EMAIL_HOST_USER,
            [settings.EMAIL_HOST_USER],
        )
        return redirect(self.success_url)


def contact_send(request):
    messages.add_message(request, messages.INFO, 'Your message has been sent successfully')
    return redirect(reverse('contact:create'))




