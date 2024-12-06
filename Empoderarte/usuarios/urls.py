from django.urls import path
from . import views


app_name = "usuarios"
urlpatterns = [
    path('cadastro/', views.cadastro_usuario, name='cadastro_usuario'),
    path('<int:usuario_id>/', views.perfil_usuario, name='perfil_usuario'),
]