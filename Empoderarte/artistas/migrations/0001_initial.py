# Generated by Django 4.2.16 on 2024-12-03 23:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('usuarios', '0002_remove_perfil_eh_artista_remove_perfil_foto'),
    ]

    operations = [
        migrations.CreateModel(
            name='Artista',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bio', models.TextField(blank=True, null=True)),
                ('usuario', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='perfil', to='usuarios.perfil')),
            ],
        ),
        migrations.CreateModel(
            name='Categorias',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(choices=[('REN', 'Renascimento'), ('REA', 'Realismo'), ('IMP', 'Impressionismo'), ('EXP', 'Expressionismo'), ('ABS', 'Abstracionismo'), ('SUR', 'Surrealismo'), ('CUB', 'Cubista'), ('ART', 'Arte Pop'), ('ARC', 'Arte Contemporânea'), ('MIN', 'Minimalismo'), ('FUT', 'Futurismo'), ('OST', 'Óleo Sobre Tela'), ('ACR', 'Acrílico'), ('AQU', 'Aquarela'), ('GUA', 'Guache')], max_length=3, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Obra',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100)),
                ('descricao', models.TextField()),
                ('preco', models.DecimalField(decimal_places=2, max_digits=10)),
                ('imagem', models.ImageField(upload_to='obras/imagens/')),
                ('disponivel', models.BooleanField(default=True)),
                ('artista', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='obras', to='artistas.artista')),
                ('categorias', models.ManyToManyField(blank=True, to='artistas.categorias')),
            ],
        ),
    ]