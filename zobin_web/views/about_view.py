from django.shortcuts import render
from django.views import View


class AboutView(View):
    def get(self, request):
        context = {
            'title': 'O nas',
        }
        return render(request, 'sites/web/about.html', context)
