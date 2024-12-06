from django import forms
from django.contrib.auth.models import User
from .models import Perfil, Interesse

# Formulário para criar o Usuário
class CadastroUsuarioForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password', 'email']  # Campos do User
        widgets = {
            'password': forms.PasswordInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'username': forms.TextInput(attrs={'class': 'form-control'}),
        }

# Formulário para o Perfil do Usuário
class PerfilForm(forms.ModelForm):
    tipo_usuario = forms.ChoiceField(
        choices=[('comum', 'Usuário Comum'), ('artista', 'Artista')],
        widget=forms.RadioSelect(attrs={'class': 'form-control'}),
        label="Tipo de Usuário"
    )
    biografia = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        required=False, label="Biografia"
    )

    class Meta:
        model = Perfil
        fields = ['data_nascimento', 'interesses', 'foto', 'tipo_usuario', 'biografia']
        widgets = {
            'data_nascimento': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'interesses': forms.CheckboxSelectMultiple(attrs={'class': 'form-check-input'}),
        }

    def __init__(self, *args, **kwargs):
        super(PerfilForm, self).__init__(*args, **kwargs)
        self.fields['biografia'].required = False  # A biografia não é obrigatória por padrão

    def clean_biografia(self):
        tipo_usuario = self.cleaned_data.get('tipo_usuario')
        biografia = self.cleaned_data.get('biografia')

        if tipo_usuario == 'artista' and not biografia:
            raise forms.ValidationError('A biografia é obrigatória para artistas.')
        
        return biografia