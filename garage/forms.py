from django import forms
from .models import Registro

class RegistroForm(forms.ModelForm):
    class Meta:
        model = Registro
        fields = ('marca','modelo','precio','descripcion','imagen','correo','vendido')
