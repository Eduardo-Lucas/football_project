from django.db import models


class Esporte(models.Model):
    nome = models.CharField(max_length=50, unique=True,
                            help_text='Indica o nome do esporte')
    ativo = models.BooleanField(default=True)
    foto = models.ImageField(upload_to='esportes', blank=True)

    def __str__(self):
        return self.nome
    
    class Meta:
        ordering = ['nome']
