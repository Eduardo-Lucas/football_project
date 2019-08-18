from django.urls import path

from apps.rodadas.views import *

urlpatterns = [
    path('list', RodadaList.as_view(), name='rodada_list'),
    path('detail/<int:pk>', RodadaDetail.as_view(), name='rodada_detail'),
    path('add', RodadaCreate.as_view(), name='rodada_create'),
    path('edit/<int:pk>', RodadaUpdate.as_view(), name='rodada_edit'),
    path('delete/<int:pk>', RodadaDelete.as_view(), name='rodada_delete'),

]
