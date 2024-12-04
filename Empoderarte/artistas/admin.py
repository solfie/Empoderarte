from django.contrib import admin

# Register your models here.
from .models import Artista, Obra, Categorias

# Register your models here.
admin.site.register(Artista)
admin.site.register(Obra)
admin.site.register(Categorias)