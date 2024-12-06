from django.contrib import admin
from artistas.models import Artista, Obra, Categorias  # Corrigido o caminho para importar de common.models

# Registrar os modelos no painel de administração
admin.site.register(Artista)
admin.site.register(Obra)
admin.site.register(Categorias)