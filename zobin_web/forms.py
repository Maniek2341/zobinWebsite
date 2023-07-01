from django import forms

from zobin_web.models import Form, Wycena


class ContactForm(forms.ModelForm):
    imie = forms.CharField(
        label='Imię',
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "autocomplete": "username",
            }
        ),
    )

    email = forms.EmailField(
        label='Adres e-mail',
        widget=forms.EmailInput(
            attrs={
                "class": "form-control",
                "autocomplete": "email",
            }
        ),
    )

    tresc = forms.CharField(
        label='Treść wiadomości',
        widget=forms.Textarea(
            attrs={
                "class": "form-control",
                "rows": 4,
                'maxlength': 255,
                'data-mdb-showcounter': 'true',
                'style': 'resize:none'
            }
        ),
    )

    dla_mnie = forms.BooleanField(
        label="Wyślij mi kopie wiadomości (opcjonalne)",
        required=False,
        widget=forms.CheckboxInput(
            attrs={
                "class": 'form-check-input me-2',
            }
        )

    )

    class Meta:
        model = Form
        fields = ['imie', 'email', 'tresc', 'dla_mnie']


class WycenaForm(forms.ModelForm):
    nazwa_firmy = forms.CharField(
        label="Nazwa firmy",
        required=True,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "autocomplete": "username",
            }
        ),
    )

    email = forms.EmailField(
        label="Email",
        required=True,
        widget=forms.EmailInput(
            attrs={
                "class": "form-control",
                "autocomplete": "email",
            }
        ),
    )

    phone = forms.IntegerField(
        label="Numer telefonu",
        required=True,
        widget=forms.NumberInput(
            attrs={
                "class": "form-control",
                "autocomplete": "phone",
            }
        ),
    )

    branza = forms.CharField(
        label="Opis branży",
        required=True,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
            }
        ),
    )

    web_page = forms.CharField(
        label="Aktualna strona WWW",
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
            }
        ),
    )

    powod_zmiany = forms.CharField(
        label="Powód zmiany",
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
            }
        ),
    )

    prod_usl = forms.CharField(
        label="Oferowane produkty/usługi",
        required=True,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
            }
        ),
    )

    konkurencja = forms.CharField(
        label="Konkurencja",
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
            }
        ),
    )

    kompletna_strona = forms.CharField(
        label="Kompletna strona internetowa",
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
            }
        ),
    )

    logo = forms.CharField(
        label="Logo",
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
            }
        ),
    )

    proj_graf = forms.CharField(
        label="Projekt graficzny",
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
            }
        ),
    )

    wdrozenie_web = forms.CharField(
        label="Wdrożenie strony internetowej",
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
            }
        ),
    )

    kodowanie_html = forms.CharField(
        label="Kodowanie HTML5+CSS3",
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
            }
        ),
    )

    makieta = forms.CharField(
        label="Makieta strony",
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
            }
        ),
    )

    elementy = forms.CharField(
        label="Elementy menu",
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
            }
        ),
    )

    animacje = forms.CharField(
        label="Animacje",
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
            }
        ),
    )

    kolorystyka = forms.CharField(
        label="Kolorystyka",
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
            }
        ),
    )

    mat_graficzne = forms.CharField(
        label="Materiały graficzne",
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
            }
        ),
    )

    tresci = forms.CharField(
        label="Treści",
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
            }
        ),
    )

    jezyki = forms.CharField(
        label="Wersje językowe",
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
            }
        ),
    )

    inspiracje = forms.CharField(
        label="Podaj strony które ci sie podobają",
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
            }
        ),
    )

    termin = forms.CharField(
        label="Termin realizacji",
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
            }
        ),
    )

    budzet_proj = forms.CharField(
        label="Budżet projektu",
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
            }
        ),
    )

    budzet_zdj = forms.CharField(
        label="Budżet na zdjęcia",
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
            }
        ),
    )

    domena = forms.CharField(
        label="Domena",
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
            }
        ),
    )

    hosting = forms.CharField(
        label="Hosting",
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
            }
        ),
    )

    co_jeszcze = forms.CharField(
        label="Co jeszcze?",
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
            }
        ),
    )

    class Meta:
        model = Wycena
        fields = '__all__'
