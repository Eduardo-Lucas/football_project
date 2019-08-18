from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from apps.equipes.models import Equipe


@admin.register(Equipe)
class EquipeResource(ImportExportModelAdmin):
    pass


