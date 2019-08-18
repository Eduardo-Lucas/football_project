from django.urls import path

from apps.campeonatos.views import *

urlpatterns = [
    path('list', CampeonatoList.as_view(), name='campeonato_list'),
    path('add', CampeonatoCreate.as_view(), name='campeonato_create'),
    path('detail/<int:pk>', CampeonatoDetail.as_view(), name='campeonato_detail'),
    path('edit/<int:pk>', CampeonatoUpdate.as_view(), name='campeonato_edit'),
    path('delete/<int:pk>', CampeonatoDelete.as_view(), name='campeonato_delete'),
    
]
