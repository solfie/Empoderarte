from django import forms
from django.contrib.auth.models import User
from .models import Perfil, Interesse

class CadastroUsuarioForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password', 'email']  # Campos do User

class PerfilForm(forms.ModelForm):
    class Meta:
        model = Perfil
        fields = ['data_nascimento', 'eh_artista', 'interesses']  # Campos do Perfil
        widgets = {
            'data_nascimento': forms.DateInput(attrs={'type': 'date'}),
            'interesses': forms.CheckboxSelectMultiple,  # Checkbox para selecionar interesses
        }