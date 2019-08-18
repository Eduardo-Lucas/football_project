from django.db import models


class Divisao(models.Model):
    nome = models.CharField(max_length=50, unique=True, help_text='Informa o nome da Divisão')
    ativo = models.BooleanField(default=True, help_text='Informa se está ativo ou não')

    def __str__(self):
        return self.nome

    class Meta:
        ordering = ['nome']    
