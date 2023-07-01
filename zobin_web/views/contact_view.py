from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.template.loader import render_to_string
from django.urls import reverse_lazy
from django.views import View

from zobinWebsite.settings import DEFAULT_FROM_EMAIL
from zobin_web.forms import ContactForm


class ContactView(View):
    def get(self, request):
        context = {
            'title': 'Kontakt',
            'contact': ContactForm()
        }
        return render(request, 'sites/web/kontakt.html', context)

    def post(self, request):

        contact_form = ContactForm(request.POST)

        context = {
            'contact': contact_form
        }

        if contact_form.is_valid():
            form = contact_form.save(commit=False)
            mail_content = {
                'imie': form.imie,
                'email': form.email,
                'tresc': form.tresc,
            }
            form.save()

            if form.dla_mnie:
                message = render_to_string('sites/mail/contact.html', mail_content)

                send_mail(
                    subject="Wiadomość potwierdzająca dla kupca",
                    message='',
                    from_email=DEFAULT_FROM_EMAIL,
                    recipient_list=[form.email],
                    fail_silently=True,
                    html_message=message
                )

                send_mail(
                    subject="Wiadomość potwierdzająca dla szefa",
                    message='',
                    from_email=DEFAULT_FROM_EMAIL,
                    recipient_list=['kontakt@zobin-it.pl'],
                    fail_silently=True,
                    html_message=message
                )

                return HttpResponseRedirect(reverse_lazy("kontakt"))

            message = render_to_string('sites/mail/contact.html', mail_content)

            send_mail(
                subject="Wiadomość potwierdzająca dla szefa1",
                message='',
                from_email=DEFAULT_FROM_EMAIL,
                recipient_list=['kontakt@zobin-it.pl'],
                fail_silently=True,
                html_message=message
            )

            return HttpResponseRedirect(reverse_lazy("kontakt"))

