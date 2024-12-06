from django.urls import path
from . import views  # Caso você tenha views a serem associadas às URLs

app_name = "artistas"
urlpatterns = [
    path('<int:artista_id>/', views.perfil_artista, name='perfil_artista'),

]