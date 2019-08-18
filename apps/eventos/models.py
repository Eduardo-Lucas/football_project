from django.db import models
from django.utils import timezone

from apps.concursos.models import Concurso
from apps.divisoes.models import Divisao
from apps.equipes.models import Equipe
from apps.rodadas.models import Rodada

STATUS_EVENTO = (
    ('Normal', 'normal'),
    ('Adiado', 'adiado'),
    ('Cancelado', 'cancelado'),
)


class Evento(models.Model):
    concurso = models.ForeignKey(Concurso, on_delete=models.CASCADE)
    sequencia = models.PositiveIntegerField(help_text='Indica o número do evento na rodada')
    data = models.DateTimeField(help_text="Informa a data e hora em que o evento vai ocorrer")
    equipe_coluna_1 = models.ForeignKey(Equipe, related_name='mandante',
                                        on_delete=models.CASCADE,
                                        help_text='Indica o dono da casa')
    equipe_coluna_2 = models.ForeignKey(Equipe, related_name='visitante',
                                        on_delete=models.CASCADE,
                                        help_text='Indica o visitante')
    
    def __str__(self):
        return str(self.sequencia)
        
    def has_started(self):
        return self.data <= timezone.now()
    
    class Meta:
        ordering = ['sequencia']
