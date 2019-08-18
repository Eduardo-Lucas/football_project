from django.db import models
from django.urls import reverse_lazy

from apps.esportes.models import Esporte
from apps.paises.models import Pais


class Campeonato(models.Model):
    pais = models.ForeignKey(Pais, on_delete=models.CASCADE)
    esporte = models.ForeignKey(Esporte, on_delete=models.CASCADE)
    nome = models.CharField(max_length=50, help_text='Nome do Campeonato')
    ano = models.PositiveIntegerField(help_text='Ano em que o Campeonato é disputado')
    ativo = models.BooleanField(default=True, help_text='Indica se o Campeonato está ativo ou não.')
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome + ' - ' + str(self.ano)

    def get_ativo(self):
        if self.ativo:
            return 'Sim'
        else:
            return 'Não'

    def get_absolute_url(self):
        return reverse_lazy('equipe_list')        

    class Meta:
        ordering = ['-ano', 'nome']
        unique_together = ['nome', 'ano']       
