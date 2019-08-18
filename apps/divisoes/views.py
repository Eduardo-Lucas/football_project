from django.shortcuts import render

from django.views.generic import ListView, DetailView, CreateView, \
    UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin 
from apps.divisoes.models import Divisao

class DivisaoList(ListView):
    model = Divisao


class DivisaoDetail(DetailView):
    model = Divisao


class DivisaoCreate(SuccessMessageMixin, CreateView):
    model = Divisao
    fields = ['nome', ]
    success_message = '%(nome)s foi criado com sucesso.'
    success_url = reverse_lazy('divisao_list')

class DivisaoUpdate(SuccessMessageMixin, UpdateView):
    model = Divisao
    fields = ['nome', 'ativo']
    success_message = '%(nome)s foi alterado com sucesso.'
    success_url = reverse_lazy('divisao_list')

class DivisaoDelete(DeleteView):
    model = Divisao
    success_url = reverse_lazy('divisao_list')