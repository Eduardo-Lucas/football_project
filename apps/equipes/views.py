from django.shortcuts import render
from apps.equipes.views import *
from django.views.generic import ListView, DetailView, CreateView, \
    UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin 
from apps.equipes.models import Equipe

class EquipeList(ListView):
    model = Equipe


class EquipeDetail(DetailView):
    model = Equipe


class EquipeCreate(SuccessMessageMixin, CreateView):
    model = Equipe
    fields = ['nome', 'nome_conhecido', 'foto']
    success_message = '%(nome)s foi criado com sucesso.'
    success_url = reverse_lazy('equipe_list')

class EquipeUpdate(SuccessMessageMixin, UpdateView):
    model = Equipe
    fields = ['nome', 'nome_conhecido', 'ativo', 'foto']
    success_message = '%(nome)s foi alterado com sucesso.'
    success_url = reverse_lazy('equipe_list')

class EquipeDelete(DeleteView):
    model = Equipe
    success_url = reverse_lazy('equipe_list')