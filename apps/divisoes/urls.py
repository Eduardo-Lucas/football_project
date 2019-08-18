from django.urls import path

from apps.divisoes.views import *

urlpatterns = [
    path('list', DivisaoList.as_view(), name='divisao_list'),
    path('detail/<int:pk>', DivisaoDetail.as_view(), name='divisao_detail'),
    path('add', DivisaoCreate.as_view(), name='divisao_create'),
    path('edit/<int:pk>', DivisaoUpdate.as_view(), name='divisao_edit'),
    path('delete/<int:pk>', DivisaoDelete.as_view(), name='divisao_delete'),
    
]
