from django.shortcuts import render, redirect
from .forms import CadastroUsuarioForm, PerfilForm
from django.contrib.auth.models import User

def cadastro_usuario(request):
    if request.method == 'POST':
        # Criação dos formulários com os dados POST
        usuario_form = CadastroUsuarioForm(request.POST)
        perfil_form = PerfilForm(request.POST)

        # Verificando se os formulários são válidos
        if usuario_form.is_valid() and perfil_form.is_valid():
            # Salvar o usuário com senha criptografada
            user = usuario_form.save(commit=False)
            user.set_password(usuario_form.cleaned_data['password'])
            user.save()

            # Salvar o perfil associado ao usuário
            perfil = perfil_form.save(commit=False)
            perfil.user = user
            perfil.save()

            # Salvar os interesses (ManyToMany)
            perfil_form.save_m2m()

            # Redirecionar para a página de login após o cadastro
            return redirect('login')  # Substitua 'login' pelo nome da sua view de login, se necessário

    else:
        # Inicialização dos formulários vazios
        usuario_form = CadastroUsuarioForm()
        perfil_form = PerfilForm()

    return render(request, 'usuarios/cadastro.html', {
        'usuario_form': usuario_form,
        'perfil_form': perfil_form
    })