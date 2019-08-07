from django.db import models


class Moeda(models.Model):
    nome = models.CharField(max_length=20, unique=True)
    simbolo = models.CharField(max_length=4)

    def __str__(self):
        return self.nome
    
    class Meta:
        ordering = ['nome']
        verbose_name = 'Moeda'
        verbose_name_plural = 'Moedas'
