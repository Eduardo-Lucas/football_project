from django.db import models
from apps.continentes.models import Continente

# TODO  Onde conseguir as bandeiras
# https://www.countries-ofthe-world.com/flags-of-the-world.html


class Pais(models.Model):
    continente = models.ForeignKey(Continente, on_delete=models.CASCADE)
    nome = models.CharField(max_length=50, unique=True,
                            help_text='Indica o nome do País')
    ativo = models.BooleanField(default=True)
    foto = models.ImageField(upload_to='paises', blank=True)

    def __str__(self):
        return self.nome
    
    def get_ativo(self):
        if self.ativo:
            return 'Sim'
        else:
            return 'Não'
    
    class Meta:
        ordering = ['nome']
        verbose_name = 'País'
        verbose_name_plural = 'Países'
