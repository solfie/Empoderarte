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
    interesses = models.ManyToManyField(Interesse, blank=True)

    def __str__(self):
        return f"Perfil de {self.user.username}"