from django.db import models


class Equipe(models.Model):
    nome = models.CharField(max_length=100, unique=True)
    endereco_url = models.URLField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.nome

    class Meta:
        ordering = ['nome']
        verbose_name = 'Equipe'
        verbose_name_plural = 'Equipes'
