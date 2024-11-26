from django.shortcuts import render, redirect
from .forms import CadastroUsuarioForm, PerfilForm
from django.contrib.auth.models import User

def cadastro_usuario(request):
    if request.method == 'POST':
        usuario_form = CadastroUsuarioForm(request.POST)
        perfil_form = PerfilForm(request.POST)

        if usuario_form.is_valid() and perfil_form.is_valid():
            # Salvar User
            user = usuario_form.save(commit=False)
            user.set_password(usuario_form.cleaned_data['password'])
            user.save()

            # Salvar Perfil
            perfil = perfil_form.save(commit=False)
            perfil.user = user
            perfil.save()
            perfil_form.save_m2m()  # Salvar os interesses (ManyToMany)

            return redirect('login')  # Redirecionar após cadastro
    else:
        usuario_form = CadastroUsuarioForm()
        perfil_form = PerfilForm()

    return render(request, 'usuarios/cadastro.html', {
        'usuario_form': usuario_form,
        'perfil_form': perfil_form
    })