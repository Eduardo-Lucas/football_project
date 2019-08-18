import django_tables2 as tables
from .models import Moeda

class MoedaTable(tables.Table):
    class Meta:
        model = Moeda
        template_name = 'django_tables2/bootstrap.html'
