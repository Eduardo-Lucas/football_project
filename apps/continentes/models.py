from django.db import models


class Continente(models.Model):
    nome = models.CharField(max_length=50, unique=True, help_text='Indica o nome do Continente')
    ativo = models.BooleanField(default=True)
    
    def __str__(self):
        return self.nome
    
    def get_ativo(self):
        if self.ativo:
            return 'Sim'
        else:
            return 'Não'
        
    class Meta:
        ordering = ['nome']
        verbose_name = 'Continente'
        verbose_name_plural = 'Continentes'
