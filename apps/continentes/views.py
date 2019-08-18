from django.views.generic import ListView, DetailView, CreateView, \
    UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin

from apps.continentes.models import Continente


class ContinenteList(ListView):
    model = Continente


class ContinenteDetail(DetailView):
    model = Continente


class ContinenteCreate(SuccessMessageMixin, CreateView):
    model = Continente
    fields = ['nome', ]
    success_message = '%(nome)s foi criado com sucesso.'
    success_url = reverse_lazy('continente_list')


class ContinenteUpdate(SuccessMessageMixin, UpdateView):
    model = Continente
    fields = ['nome', 'ativo', ]
    success_message = '%(nome)s foi alterado com sucesso.'
    success_url = reverse_lazy('continente_list')


class ContinenteDelete(DeleteView):
    model = Continente
    success_url = reverse_lazy('continente_list')
