from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from .forms import CadastroUsuarioForm, PerfilForm

def cadastro_usuario(request):
    if request.method == 'POST':
        user_form = CadastroUsuarioForm(request.POST)
        perfil_form = PerfilForm(request.POST)
        
        if user_form.is_valid() and perfil_form.is_valid():
            # Salvar o usuário
            user = user_form.save(commit=False)  # Não salva ainda
            user.password = make_password(user.password)  # Criptografar a senha
            user.save()  # Agora salva

            # Salvar o perfil
            perfil = perfil_form.save(commit=False)  # Não salva ainda
            perfil.user = user  # Associa o perfil ao usuário criado
            perfil.save()  # Agora salva
            perfil_form.save_m2m()  # Salva os relacionamentos de ManyToMany, como interesses

            return redirect('/common/indexDeslogado/')  # Redireciona para uma página de sucesso
    else:
        user_form = CadastroUsuarioForm()
        perfil_form = PerfilForm()

    return render(request, 'usuarios/cadastro.html', {
    'user_form': user_form,
    'perfil_form': perfil_form,
})

