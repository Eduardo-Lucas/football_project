from django.urls import path

from apps.eventos.views import *

urlpatterns = [
    path('list', EventoList.as_view(), name='evento_list'),
    path('detail/<int:pk>', EventoDetail.as_view(), name='evento_detail'),
    path('add', EventoCreate.as_view(), name='evento_create'),
    path('edit/<int:pk>', EventoUpdate.as_view(), name='evento_edit'),
    path('delete/<int:pk>', EventoDelete.as_view(), name='evento_delete'),

]
