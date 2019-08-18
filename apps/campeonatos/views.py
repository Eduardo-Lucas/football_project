from django.views.generic import ListView, CreateView, DetailView, \
    DeleteView, UpdateView
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin 

from apps.campeonatos.models import Campeonato    

from django.shortcuts import render


class CampeonatoList(ListView):
    model = Campeonato 


class CampeonatoDetail(DetailView):
    model = Campeonato


class CampeonatoCreate(SuccessMessageMixin, CreateView):
    model = Campeonato 
    fields = ['nome', 'ano', 'esporte', 'pais']
    success_message = '%(nome)s foi cadastrado com sucesso!'
    success_url = reverse_lazy('campeonato_list')


class CampeonatoUpdate(SuccessMessageMixin, UpdateView):
    model = Campeonato 
    fields = ['nome', 'ano', 'esporte', 'pais', 'ativo']
    success_message = '%(nome)s foi atualizado com sucesso!'
    success_url = reverse_lazy('campeonato_list')


class CampeonatoDelete(SuccessMessageMixin, DeleteView):
    model = Campeonato 
    success_message = 'O registro foi apagado com sucesso!'
    success_url = reverse_lazy('campeonato_list')
