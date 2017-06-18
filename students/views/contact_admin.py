import logging
from django.contrib import messages
from django.core.mail import send_mail
from django.utils.translation import ugettext as _
from django.views.generic.edit import FormView

from config.settings import ADMINS
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
            send_mail(subject, message, from_email, [admin[1] for admin in ADMINS])
        except Exception:
            messages.add_message(
                self.request,
                messages.INFO,
                _('Something went wrong. Please, try again later')
            )

            logger = logging.getLogger(__name__)
            logger.exception(message)
        else:
            messages.add_message(
                self.request,
                messages.INFO,
                _('Your message was successfully sent')
            )
        return super(ContactView, self).form_valid(form)
