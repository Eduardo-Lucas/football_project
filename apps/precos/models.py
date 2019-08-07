from django.db import models

from apps.jogadores.models import Jogador
from apps.moedas.models import Moeda


class Preco(models.Model):
    jogador = models.ForeignKey(Jogador, on_delete=models.CASCADE)
    moeda = models.ForeignKey(Moeda, on_delete=models.CASCADE)
    dia = models.DateField()
    compra = models.DecimalField(max_length=16, max_digits=16, decimal_places=2, default=0)
    venda = models.DecimalField(max_length=16, max_digits=16, decimal_places=2, default=0)

    def valor_compra(self):
        return self.moeda + ' ' + self.compra

    def valor_venda(self):
        return self.moeda + ' ' + self.venda
    
    def __str__(self):
        return self.jogador
