from django.urls import path

from apps.concursos.views import *

urlpatterns = [
    path('list', ConcursoList.as_view(), name='concurso_list'),
    path('detail/<int:pk>', ConcursoDetail.as_view(), name='concurso_detail'),
    path('add', ConcursoCreate.as_view(), name='concurso_create'),
    path('edit/<int:pk>', ConcursoUpdate.as_view(), name='concurso_edit'),
    path('delete/<int:pk>', ConcursoDelete.as_view(), name='concurso_delete'),

]
