
from django.views.generic import ListView, DetailView, CreateView, \
    UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin

from apps.rodadas.models import Rodada


class RodadaList(ListView):
    model = Rodada


class RodadaDetail(DetailView):
    model = Rodada


class RodadaCreate(SuccessMessageMixin, CreateView):
    model = Rodada
    fields = ['numero', 'campeonato', ]
    success_message = 'A rodada de número %(numero)s foi criada com sucesso.'
    success_url = reverse_lazy('rodada_list')


class RodadaUpdate(SuccessMessageMixin, UpdateView):
    model = Rodada
    fields = ['numero', 'campeonato', 'ativo', ]
    success_message = 'A rodada de número %(numero)s foi alterada com sucesso.'
    success_url = reverse_lazy('rodada_list')


class RodadaDelete(DeleteView):
    model = Rodada
    success_url = reverse_lazy('rodada_list')
