
from django.views.generic import ListView, DetailView, CreateView, \
    UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin

from apps.paises.models import Pais


class PaisList(ListView):
    model = Pais


class PaisDetail(DetailView):
    model = Pais


class PaisCreate(SuccessMessageMixin, CreateView):
    model = Pais
    fields = ['nome', 'foto', 'continente']
    success_message = '%(nome)s foi criado com sucesso.'
    success_url = reverse_lazy('pais_list')


class PaisUpdate(SuccessMessageMixin, UpdateView):
    model = Pais
    fields = ['nome', 'ativo', 'continente', 'foto']
    success_message = '%(nome)s foi alterado com sucesso.'
    success_url = reverse_lazy('pais_list')


class PaisDelete(DeleteView):
    model = Pais
    success_url = reverse_lazy('pais_list')
