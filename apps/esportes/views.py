
from django.views.generic import ListView, DetailView, CreateView, \
    UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin

from apps.esportes.models import Esporte


class EsporteList(ListView):
    model = Esporte


class EsporteDetail(DetailView):
    model = Esporte


class EsporteCreate(SuccessMessageMixin, CreateView):
    model = Esporte
    fields = ['nome', 'foto']
    success_message = '%(nome)s foi criado com sucesso.'
    success_url = reverse_lazy('esporte_list')


class EsporteUpdate(SuccessMessageMixin, UpdateView):
    model = Esporte
    fields = ['nome', 'ativo', 'foto']
    success_message = '%(nome)s foi alterado com sucesso.'
    success_url = reverse_lazy('esporte_list')


class EsporteDelete(DeleteView):
    model = Esporte
    success_url = reverse_lazy('esporte_list')
