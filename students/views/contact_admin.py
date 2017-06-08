from django.shortcuts import render
from django.contrib import messages
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views.generic.edit import FormView

from config.settings import ADMIN_EMAIL
from students.forms import ContactForm


class ContactView(FormView):

    template_name = 'contact_admin/form.html'
    form_class = ContactForm
    success_url = '/contact-admin/'

    def form_valid(self, form):
        subject = form.cleaned_data['subject']
        message = form.cleaned_data['message']
        from_email = form.cleaned_data['from_email']
        try:
            send_mail(subject, message, from_email, [ADMIN_EMAIL])
        except Exception:
            messages.add_message(
                self.request,
                messages.INFO,
                'Щось пiшло не так, будь ласка спробуйте пiзнiше'
            )
        else:
            messages.add_message(
                self.request,
                messages.INFO,
                'Ваше повідомлення будо успішно надіслане'
            )
        return super(ContactView, self).form_valid(form)
