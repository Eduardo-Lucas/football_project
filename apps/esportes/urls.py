from django.urls import path

from apps.esportes.views import *

urlpatterns = [
    path('list', EsporteList.as_view(), name='esporte_list'),
    path('detail/<int:pk>', EsporteDetail.as_view(), name='esporte_detail'),
    path('add', EsporteCreate.as_view(), name='esporte_create'),
    path('edit/<int:pk>', EsporteUpdate.as_view(), name='esporte_edit'),
    path('delete/<int:pk>', EsporteDelete.as_view(), name='esporte_delete'),

]
