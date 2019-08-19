from django.contrib import messages
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import Q
from django.forms import modelformset_factory
from django.shortcuts import render, redirect

from django.views.generic import ListView, DetailView, CreateView, \
    UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin 
from apps.equipes.models import Equipe

# TODO Onde conseguir os icones das Equipes
# https://www.gazetaesportiva.com/campeonatos/brasileiro-serie-a/


def equipe_add(request):
    qtd_equipes = Equipe.objects.count()
    equipeformset = modelformset_factory(Equipe, fields=('nome', 'nome_conhecido', 'divisao', 'foto'),
                                         extra=5,)
    if request.method == 'POST':
        form = equipeformset(request.POST)
        # instances = form.save(commit=False)
        # for instance in instances:
        #     instance.save()
        
        form.save()
        messages.success(request, 'Registro atualizado com sucesso.')

        return redirect('equipe_add', )

    form = equipeformset()
    
    return render(request, 'equipes/equipe_add.html', {'form': form,
                                                       'qtd_equipes': qtd_equipes})


class EquipeList(ListView):
    model = Equipe
    template_name = 'equipes/equipe_list.html'
    
    def get_queryset(self):
        valor = self.request.GET.get('q')
        if valor:
            object_list = self.model.objects.filter(
                Q(nome__icontains=valor) |
                Q(nome_conhecido__icontains=valor)
            )
        else:
            object_list = self.model.objects.all()

        paginator = Paginator(object_list, 9)  # Show 9 produtos per page

        page = self.request.GET.get('page')
        try:
            queryset = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            queryset = paginator.page(1)
        except EmptyPage:
            # If page is out of range (e.g. 9999), deliver last page of results.
            queryset = paginator.page(paginator.num_pages)

        # return object_list
        return queryset


class EquipeDetail(DetailView):
    model = Equipe


class EquipeCreate(SuccessMessageMixin, CreateView):
    model = Equipe
    fields = ['nome', 'nome_conhecido', 'divisao', 'foto']
    success_message = '%(nome)s foi criado com sucesso.'
    success_url = reverse_lazy('equipe_list')


class EquipeUpdate(SuccessMessageMixin, UpdateView):
    model = Equipe
    fields = ['nome', 'nome_conhecido', 'divisao', 'ativo', 'foto']
    success_message = '%(nome)s foi alterado com sucesso.'
    success_url = reverse_lazy('equipe_list')


class EquipeDelete(DeleteView):
    model = Equipe
    success_url = reverse_lazy('equipe_list')