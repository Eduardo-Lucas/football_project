from django.db import models

from apps.divisoes.models import Divisao


class Equipe(models.Model):
    nome = models.CharField(max_length=100, unique=True)
    nome_conhecido = models.CharField(max_length=20, blank=True, null=True)
    endereco_url = models.URLField(max_length=100, blank=True, null=True)
    foto = models.ImageField(upload_to='equipes', blank=True)   
    ativo = models.BooleanField(default=True)

    def __str__(self):
        return self.nome_conhecido

    def get_ativo(self):
        if self.ativo:
            return 'Sim'
        else:
            return 'Não'    

    class Meta:
        ordering = ['nome_conhecido']
        verbose_name = 'Equipe'
        verbose_name_plural = 'Equipes'
