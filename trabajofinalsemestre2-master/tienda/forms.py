from django import forms
from .models import Zapato

class ZapatoForm(forms.ModelForm):
    class Meta:
        model = Zapato
        fields = ['nombre','descripcion','tipo','precio','color','talla','marca','puntuacion','imagen']
