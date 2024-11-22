from django.db import models
from django.contrib.auth.models import User

# INTERESSES DO USUÁRIO
class Interesse(models.Model):
    FEMINISMO = 'FEM'
    ESCULTURA = 'ESC'
    ABSTRATO = 'ABS'
    EMOÇOES = 'EMO'
    DESENHO = 'DES'
    LITERATURA = 'LIT'
    FOTOGRAFIA = 'FOT'
    GRAFITTI = 'GRA'


    SETORES_CHOICES = [
        (FEMINISMO, 'Feminismo'),
        (ESCULTURA, 'Escultura'),
        (ABSTRATO, 'Abstrato'),
        (EMOÇOES, 'Emoções'),
        (DESENHO, 'Desenho'),
        (LITERATURA, 'Literatura'),
        (FOTOGRAFIA, 'Fotografia'),
        (GRAFITTI, 'Grafitti'),
        # Outras opções de interesse podem ser add
    ]


# Modelo de Perfil de Usuário
class Perfil(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='perfil')  # Relacionamento 1-para-1 com User
    foto = models.ImageField(upload_to='fotos_perfis/', blank=True, null=True)  # Foto de perfil
    data_nascimento = models.DateField(null=True, blank=True)  # Data de nascimento
    eh_artista = models.BooleanField(default=False)  # Boolean se é artista ou usuário comum
    interesses = models.ManyToManyField(Interesse, blank=True)  # Interesses do usuário

    def __str__(self):
        return f"Perfil de {self.user.username}"
