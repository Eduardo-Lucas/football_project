from django.forms import inlineformset_factory
from django.shortcuts import redirect, render
from django.views.generic import ListView, DetailView, CreateView, \
    UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin

from apps.concursos.models import Concurso
from apps.eventos.models import Evento


def concurso_add(request, concurso_id):
    concurso = Concurso.objects.get(pk=concurso_id)
    evento_formset = inlineformset_factory(Concurso, Evento,
                                           fields=('sequencia', 'data', 'equipe_coluna_1', 'equipe_coluna_2',),
                                           max_num=14, extra=1)
    
    if request.method == 'POST':
        formset = evento_formset(request.POST, instance=concurso)
        if formset.is_valid():
            formset.save()
            
            return redirect('concurso_add', concurso_id=concurso.id)

    formset = evento_formset(instance=concurso)
    return render(request, 'concursos/concurso_add.html', {'formset': formset,
                                                           'concurso': concurso})


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
