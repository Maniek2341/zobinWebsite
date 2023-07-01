from django.shortcuts import render
from django.views import View


class PortfolioView(View):
    def get(self, request):
        context = {
            'title': 'Portfolio',
        }
        return render(request, 'sites/web/portfolio.html', context)
