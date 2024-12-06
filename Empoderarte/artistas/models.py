from django.db import models
from usuarios.models import Perfil

class Artista(models.Model):
    usuario = models.OneToOneField(Perfil, on_delete=models.CASCADE, related_name='perfil')  # Relacionamento 1-para-1 com User
    def __str__(self):
        return f"Artista: {self.usuario.user.username}"


class Categorias(models.Model):
    RENASCIMENTO = 'REN'
    REALISMO = 'REA'
    IMPRESSIONISMO = 'IMP'
    EXPRESSIONISMO = 'EXP'
    ABSTRACIONISMO = 'ABS'
    SURREALISMO = 'SUR'
    CUBISMO = 'CUB'
    ARTEPOP = 'ART'
    ARTECONTEMPORÂNEA = 'ARC'
    MINIMALISMO = 'MIN'
    FUTURISMO = 'FUT'
    ÓLEOSOBRETELA = 'OST'
    ACRILICO = 'ACR'
    AQUARELA = 'AQU'
    GUACHE = 'GUA'

    SETORES_CHOICES = [
        (RENASCIMENTO, 'Renascimento'),
        (REALISMO, 'Realismo'),
        (IMPRESSIONISMO, 'Impressionismo'),
        (EXPRESSIONISMO, 'Expressionismo'),
        (ABSTRACIONISMO, 'Abstracionismo'),
        (SURREALISMO, 'Surrealismo'),
        (CUBISMO, 'Cubista'),
        (ARTEPOP, 'Arte Pop'),
        (ARTECONTEMPORÂNEA, 'Arte Contemporânea'),
        (MINIMALISMO, 'Minimalismo'),
        (FUTURISMO, 'Futurismo'),
        (ÓLEOSOBRETELA, 'Óleo Sobre Tela'),
        (ACRILICO, 'Acrílico'),
        (AQUARELA, 'Aquarela'),
        (GUACHE, 'Guache'),
    ]

    nome = models.CharField(max_length=3, choices=SETORES_CHOICES, unique=True)

    def __str__(self):
        return dict(self.SETORES_CHOICES).get(self.nome, self.nome)


class Obra(models.Model):
    artista = models.ForeignKey(Artista, on_delete=models.CASCADE, related_name='obras')
    titulo = models.CharField(max_length=100)
    descricao = models.TextField()
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    imagem = models.ImageField(upload_to='static/img/')
    disponivel = models.BooleanField(default=True)  # Corrigido
    categorias = models.ManyToManyField(Categorias, blank=True)

    def __str__(self):
        return self.titulo