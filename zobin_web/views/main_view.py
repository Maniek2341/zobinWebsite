from django.shortcuts import render
from django.views import View


class MainView(View):
    def get(self, request):
        context = {
            'title': 'Tworzenie stron internetowych',
        }
        return render(request, 'sites/web/main.html', context)
