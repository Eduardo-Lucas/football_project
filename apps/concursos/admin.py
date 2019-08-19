from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from apps.concursos.models import Concurso


@admin.register(Concurso)
class ConcursoResource(ImportExportModelAdmin):
    pass

