from django.views.generic import ListView, DetailView, CreateView, \
    UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin

from apps.eventos.models import Evento


class EventoList(ListView):
    model = Evento


class EventoDetail(DetailView):
    model = Evento


class EventoCreate(SuccessMessageMixin, CreateView):
    model = Evento
    fields = ['concurso', 'sequencia', 'data', 'equipe_coluna_1', 'equipe_coluna_2', ]
    success_message = 'O evento de número %(sequencia)s foi criada com sucesso.'
    success_url = reverse_lazy('evento_list')


class EventoUpdate(SuccessMessageMixin, UpdateView):
    model = Evento
    fields = ['concurso', 'sequencia', 'data', 'equipe_coluna_1', 'equipe_coluna_2',
              'ativo', 'status', 'nova_data']
    success_message = 'O evento de número %(sequencia)s foi alterado com sucesso.'
    success_url = reverse_lazy('evento_list')


class EventoDelete(DeleteView):
    model = Evento
    success_url = reverse_lazy('evento_list')
