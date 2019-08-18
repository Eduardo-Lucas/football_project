from django.urls import path

from apps.equipes.views import *

urlpatterns = [
    path('list', EquipeList.as_view(), name='equipe_list'),
    path('detail/<int:pk>', EquipeDetail.as_view(), name='equipe_detail'),
    path('add', EquipeCreate.as_view(), name='equipe_create'),
    path('edit/<int:pk>', EquipeUpdate.as_view(), name='equipe_edit'),
    path('delete/<int:pk>', EquipeDelete.as_view(), name='equipe_delete'),
    
]
