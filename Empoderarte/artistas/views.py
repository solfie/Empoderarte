from django.shortcuts import render, get_object_or_404
from artistas.models import Artista, Obra


# View para a página index_deslogado
def perfil_artista (request, artista_id):
    artista = get_object_or_404(Artista, pk=artista_id)
    return render (request, "artistas/perfil_artista.html", {"artista": artista})