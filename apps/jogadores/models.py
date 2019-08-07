from django.db import models

from apps.equipes.models import Equipe

chuta = (
    ('Direito', 'Direito'),
    ('Esquerdo', 'Esquerdo')
)


class Jogador(models.Model):
    equipe = models.ForeignKey(Equipe, on_delete=models.CASCADE)
    nome = models.CharField(max_length=50, unique=True)
    foto = models.ImageField(upload_to='jogadores', blank=True)
    posicao = models.CharField(max_length=20)
    data_nascimento = models.DateField(blank=True, null=True)
    local_nascimento = models.CharField(max_length=50, blank=True, null=True)
    pais = models.CharField(max_length=20, blank=True, null=True)
    chuta_com_pe = models.CharField(max_length=10, choices=chuta, default='Direito')
    peso = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    altura = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    numero_camisa = models.PositiveIntegerField(blank=True, null=True)
    em_atividade = models.BooleanField(default=True)
    
    def __str__(self):
        return self.nome
    
    class Meta:
        verbose_name = 'Jogador'
        verbose_name_plural = 'Jogadores'

