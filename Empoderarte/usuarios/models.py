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
    ]

    nome = models.CharField(max_length=3, choices=SETORES_CHOICES, unique=True)

    def __str__(self):
        return dict(self.SETORES_CHOICES).get(self.nome, self.nome)


class Perfil(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='perfil')
    data_nascimento = models.DateField(null=True, blank=True)
    interesses = models.ManyToManyField(Interesse, blank=True)  # Relacionamento com Interesse
    foto = models.ImageField(upload_to='perfil_fotos/', null=True, blank=True)  # Foto de perfil
    tipo_usuario = models.CharField(max_length=10, choices=[('comum', 'Usuário Comum'), ('artista', 'Artista')], default='comum')  # Tipo de usuário
    biografia = models.TextField(null=True, blank=True)  # Biografia para artistas

    def __str__(self):
        return f"Perfil de {self.user.username}"