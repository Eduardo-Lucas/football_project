from django.contrib import messages
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
    jogos_cadastrados = concurso.evento_set.count()
    jogos_a_cadastrar = concurso.num_max_jogos - jogos_cadastrados
    
    evento_formset = inlineformset_factory(Concurso, Evento,
                                           fields=('sequencia', 'data', 'equipe_coluna_1', 'equipe_coluna_2',),
                                           max_num=concurso.num_max_jogos, extra=1)
        
    if request.method == 'POST':
        formset = evento_formset(request.POST, instance=concurso)
        if formset.is_valid():
            formset.save()
            messages.success(request, 'Registro atualizado com sucesso.')
            
            return redirect('concurso_add', concurso_id=concurso.id)

    formset = evento_formset(instance=concurso)
    return render(request, 'concursos/concurso_add.html', {'formset': formset,
                                                           'concurso': concurso,
                                                           'jogos_cadastrados': jogos_cadastrados,
                                                           'jogos_a_cadastrar': jogos_a_cadastrar,
                                                           })


class ConcursoList(ListView):
    model = Concurso


class ConcursoDetail(DetailView):
    model = Concurso


class ConcursoCreate(SuccessMessageMixin, CreateView):
    model = Concurso
    fields = ['numero', 'abertura', 'encerramento', 'num_max_jogos', ]
    success_message = 'O concurso de número %(numero)s foi criado com sucesso.'
    success_url = reverse_lazy('concurso_list')


class ConcursoUpdate(SuccessMessageMixin, UpdateView):
    model = Concurso
    fields = ['numero', 'abertura', 'encerramento', 'ativo', 'num_max_jogos', ]
    success_message = 'O concurso de número %(numero)s foi alterado com sucesso.'
    success_url = reverse_lazy('concurso_list')


class ConcursoDelete(DeleteView):
    model = Concurso
    success_url = reverse_lazy('concurso_list')
