from import_export import resources

from apps.equipes.models import Equipe


class EquipeResource(resources.ModelResource):
    class Meta:
        model = Equipe
        fields = '__all__'
