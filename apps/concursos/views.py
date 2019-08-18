from django.views.generic import ListView, DetailView, CreateView, \
    UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin

from apps.concursos.models import Concurso


class ConcursoList(ListView):
    model = Concurso


class ConcursoDetail(DetailView):
    model = Concurso


class ConcursoCreate(SuccessMessageMixin, CreateView):
    model = Concurso
    fields = ['numero', 'abertura', 'encerramento']
    success_message = 'O concurso de número %(numero)s foi criado com sucesso.'
    success_url = reverse_lazy('concurso_list')


class ConcursoUpdate(SuccessMessageMixin, UpdateView):
    model = Concurso
    fields = ['numero', 'abertura', 'encerramento', 'ativo']
    success_message = 'O concurso de número %(numero)s foi alterado com sucesso.'
    success_url = reverse_lazy('concurso_list')


class ConcursoDelete(DeleteView):
    model = Concurso
    success_url = reverse_lazy('concurso_list')
