from django.shortcuts import render
from django.views import View


class PolitykaView(View):
    def get(self, request):
        context = {
            'title': 'Polityka Prywatności',
        }
        return render(request, 'sites/web/polityka.html', context)
