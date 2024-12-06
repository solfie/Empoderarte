from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.contrib.auth import login  # Para fazer login automático
from .forms import CadastroUsuarioForm, PerfilForm
from .models import Perfil

def cadastro_usuario(request):
    if request.method == 'POST':
        user_form = CadastroUsuarioForm(request.POST)
        perfil_form = PerfilForm(request.POST, request.FILES)  # 'request.FILES' para fotos

        if user_form.is_valid() and perfil_form.is_valid():
            # Criação do usuário
            user = user_form.save(commit=False)
            user.password = make_password(user.password)  # Criptografa a senha
            user.save()

            # Criação do perfil
            perfil = perfil_form.save(commit=False)
            perfil.user = user  # Associa o perfil ao usuário criado
            perfil.save()

            perfil_form.save_m2m()  # Salva os interesses ManyToMany

            # Login automático após o cadastro
            login(request, user)

            return redirect('/common/indexDeslogado/')  # Redireciona para a página de sucesso
    else:
        user_form = CadastroUsuarioForm()
        perfil_form = PerfilForm()

    return render(request, 'usuarios/cadastro.html', {
        'user_form': user_form,
        'perfil_form': perfil_form,
    })

def perfil_usuario(request, usuario_id):
    usuario = get_object_or_404(Perfil, user__id=usuario_id)
    return render(request, "usuarios/perfil_usuario.html", {"usuario": usuario})
