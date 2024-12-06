# common/models.py
from django.db import models

# # Modelo para Artista
# class Artista(models.Model):
#     nome = models.CharField(max_length=200)
#     biografia = models.TextField(blank=True, null=True)

#     def __str__(self):
#         return self.nome

# Modelo para Obra de Arte
# class Obra(models.Model):
#     titulo = models.CharField(max_length=200)
#     descricao = models.TextField(blank=True, null=True)
#     imagem = models.ImageField(upload_to='obras/', blank=True, null=True)  # Imagem da obra
#     artista = models.ForeignKey(Artista, related_name='obras', on_delete=models.CASCADE)  # Relaciona com o Artista

#     def __str__(self):
#         return self.titulo