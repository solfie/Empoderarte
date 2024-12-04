# common/views.py
from django.shortcuts import render
from artistas.models import Artista, Obra

# View para a página index_deslogado
def index_deslogado(request):
    artistas = Artista.objects.all()  # Busca todos os artistas
    obras = Obra.objects.all()  # Busca todas as obras
    return render(request, 'common/indexDeslogado.html', {
        'artistas': artistas,
        'obras': obras
    })