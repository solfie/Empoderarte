from django import forms
from django.contrib.auth.models import User
from .models import Perfil, Interesse

class CadastroUsuarioForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password', 'email']  # Campos do User
        widgets = {
            'password': forms.PasswordInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'username': forms.TextInput(attrs={'class': 'form-control'}),
        }

class PerfilForm(forms.ModelForm):
    tipo_usuario = forms.ChoiceField(
        choices=[('artista', 'Artista'), ('cliente', 'Cliente')],
        widget=forms.RadioSelect(attrs={'class': 'form-control'}),
        label="Tipo de Usuário"
    )
    class Meta:
        model = Perfil
        fields = ['data_nascimento', 'interesses']  # Campos do Perfil
        widgets = {
            'data_nascimento': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'interesses': forms.CheckboxSelectMultiple(attrs={'class': 'form-check-input'}),
        }