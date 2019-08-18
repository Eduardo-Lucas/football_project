from django.db import models

from apps.campeonatos.models import Campeonato


class Rodada(models.Model):
    numero = models.PositiveIntegerField(help_text='Indica o número da Rodada')
    campeonato = models.ForeignKey(Campeonato, on_delete=models.CASCADE)
    ativo = models.BooleanField(default=True)
    
    def __str__(self):
        return 'Rodada de número ' + str(self.numero)
    
    class Meta:
        ordering = ['campeonato', 'numero', '-ativo']
        unique_together = ['campeonato', 'numero']
