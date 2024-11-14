from django.db import models

class Artista(models.Model):
    nome = models.CharField(max_length=100)
    usuario = models.CharField(max_length=50)
    bio = models.TextField(null=True, blank=True)  # Torna o campo bio opcional
    data_nascimento = models.DateField
    foto = models.ImageField(upload_to='artistas/fotos/', null=True, blank=True)  # Torna o campo foto opcional

    def __str__(self):
        return self.usuario

class Obra(models.Model):
    artista = models.ForeignKey(Artista, on_delete=models.CASCADE, related_name='obras')
    titulo = models.CharField(max_length=100)
    descricao = models.TextField()
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    imagem = models.ImageField(upload_to='obras/imagens/')
    disponivel = models.BooleanField

    def __str__(self):
        return self.titulo