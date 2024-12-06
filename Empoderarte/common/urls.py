# common/urls.py
from django.urls import path
from . import views  # Caso você tenha views a serem associadas às URLs
app_name = "common"
# Aqui você pode definir as URLs que pertencem à aplicação 'common'
urlpatterns = [
    path('indexDeslogado/', views.index_deslogado, name='indexDeslogado'),
]