from django.db import models


class Concurso(models.Model):
    numero = models.PositiveIntegerField(unique=True,
                                         help_text='Indica o número do concurso')
    abertura = models.DateTimeField(help_text='Abertura das apostas')
    encerramento = models.DateTimeField(help_text='Encerramento das apostas')
    ativo = models.BooleanField(default=True,
                                help_text='Indica se o Concurso ainda aceita apostas.')
    
    def __str__(self):
        return str(self.numero)
    
    class Meta:
        ordering = ['numero']
