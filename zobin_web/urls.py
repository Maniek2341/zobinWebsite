from django.urls import path
from zobin_web.views import MainView, ContactView, WWWView, WycenaView, AboutView, PortfolioView, PolitykaView

urlpatterns = [
    path('', MainView.as_view(), name='main'),
    path('kontakt', ContactView.as_view(), name='kontakt'),
    path('www', WWWView.as_view(), name='www'),
    path('wycena', WycenaView.as_view(), name='wycena'),
    path('o-nas', AboutView.as_view(), name='about'),
    path('portfolio', PortfolioView.as_view(), name='portfolio'),
    path('polityka-prywatności', PolitykaView.as_view(), name='polityka'),
]