
from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', include('apps.core.urls')),
    path('campeonatos/', include('apps.campeonatos.urls')),
    path('concursos/', include('apps.concursos.urls')),
    path('continentes/', include('apps.continentes.urls')),
    path('divisoes/', include('apps.divisoes.urls')),
    path('equipes/', include('apps.equipes.urls')),
    path('eventos/', include('apps.eventos.urls')),
    path('esportes/', include('apps.esportes.urls')),
    path('paises/', include('apps.paises.urls')),
    path('rodadas/', include('apps.rodadas.urls')),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
