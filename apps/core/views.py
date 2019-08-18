from django.shortcuts import render
from django_tables2 import RequestConfig

from apps.equipes.models import Equipe
from apps.moedas.models import Moeda
from apps.moedas.tables import MoedaTable


def home(request):
    equipes = Equipe.objects.all()
    return render(request, 'core/index.html', {'equipes': equipes})


def moeda(request):
    table = MoedaTable(Moeda.objects.all())
    RequestConfig(request).configure(table)
    return render(request, 'core/moeda.html', {'table': table})
