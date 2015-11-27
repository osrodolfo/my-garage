from django import forms
from .models import Registro
from django.contrib.auth.models import User

class RegistroForm(forms.ModelForm):
    class Meta:
        model = Registro
        fields = ('marca','modelo','precio','descripcion','imagen','correo','vendido')

class LoginForm(forms.Form):
    username=forms.CharField()
    password=forms.CharField(widget=forms.PasswordInput())

class RegistroUserForm(forms.Form):

    username = forms.CharField(min_length=4)
    password = forms.CharField(min_length=4, widget=forms.PasswordInput())
    password2 = forms.CharField(widget=forms.PasswordInput())

    def clean_username(self):
        username = self.cleaned_data['username']
        if User.objects.filter(username=username):
            raise forms.ValidationError('Nombre de usuario ya registrado.')
        return username

    def clean_password2(self):
        password = self.cleaned_data['password']
        password2 = self.cleaned_data['password2']
        if password != password2:
            raise forms.ValidationError('Las contraseñas no coinciden.')
        return password2
