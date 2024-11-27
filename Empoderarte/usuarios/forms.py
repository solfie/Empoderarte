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
            'data_nascimento': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),  # Definir o widget do campo como um input de data
            'interesses': forms.CheckboxSelectMultiple(attrs={'class': 'form-control'}),  # Checkbox para selecionar interesses
        }
    
    # Adicionando o campo para selecionar tipo de usuário (Artista ou Cliente)
    tipo_usuario = forms.ChoiceField(
        choices=[('artista', 'Artista'), ('cliente', 'Cliente')],
        widget=forms.RadioSelect(attrs={'class': 'form-control'}),
        label="Tipo de Usuário"
    )