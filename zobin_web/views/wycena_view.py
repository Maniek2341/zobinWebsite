from django.shortcuts import render
from django.views import View

from zobin_web.forms import ContactForm, WycenaForm


class WycenaView(View):
    def get(self, request):
        context = {
            'title': 'Wycena',
            'wycena': WycenaForm()
        }
        return render(request, 'sites/web/wycena.html', context)
