from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from .forms import CadastroUsuarioForm, PerfilForm
from .models import Perfil

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

from django.shortcuts import render, get_object_or_404
# from usuarios.models import usuarios, Obra
# View para a página index_deslogado
def perfil_usuario (request, usuario_id):
    usuario = get_object_or_404(Perfil, user__id=usuario_id)
    return render (request, "usuarios/perfil_usuario.html", {"usuario": usuario})

    

