from django.shortcuts import render
from django.views import View


class WWWView(View):
    def get(self, request):
        context = {
            'title': 'Oferta tworzenia stron WWW',
        }
        return render(request, 'sites/web/www.html', context)
