from django.db import models


# Create your models here.

class Form(models.Model):
    imie = models.CharField(max_length=50)
    email = models.EmailField()
    tresc = models.TextField(max_length=255)
    dla_mnie = models.BooleanField(null=True)

    class Meta:
        verbose_name = 'Formularz kontaktowy'
        verbose_name_plural = 'Formularze kontaktowe'

    def __str__(self):
        return "Formularz od: %s" % self.email

class Wycena(models.Model):
    nazwa_firmy = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone = models.IntegerField()
    branza = models.CharField(max_length=100)
    web_page = models.TextField(max_length=250)
    powod_zmiany = models.TextField(max_length=300)
    prod_usl = models.CharField(max_length=200)
    konkurencja = models.CharField(max_length=200)
    kompletna_strona = models.CharField(max_length=1)
    logo = models.CharField(max_length=1)
    proj_graf = models.CharField(max_length=1)
    wdrozenie_web = models.CharField(max_length=1)
    kodowanie_html = models.CharField(max_length=1)
    makieta = models.CharField(max_length=1)
    elementy = models.CharField(max_length=200)
    animacje = models.CharField(max_length=200)
    kolorystyka = models.CharField(max_length=200)
    mat_graficzne = models.CharField(max_length=200)
    tresci = models.CharField(max_length=200)
    jezyki = models.CharField(max_length=200)
    inspiracje = models.CharField(max_length=200)
    termin = models.CharField(max_length=200)
    budzet_proj = models.CharField(max_length=200)
    budzet_zdj = models.CharField(max_length=200)
    domena = models.CharField(max_length=100)
    hosting = models.CharField(max_length=200)
    co_jeszcze = models.CharField(max_length=200)


    class Meta:
        verbose_name = 'Wycena'
        verbose_name_plural = 'Wyceny'

    def __str__(self):
        return "Wycena od: %s" % self.email

