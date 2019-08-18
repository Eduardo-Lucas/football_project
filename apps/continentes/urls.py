from django.urls import path

from apps.continentes.views import *

urlpatterns = [
    path('list', ContinenteList.as_view(), name='continente_list'),
    path('detail/<int:pk>', ContinenteDetail.as_view(), name='continente_detail'),
    path('add', ContinenteCreate.as_view(), name='continente_create'),
    path('edit/<int:pk>', ContinenteUpdate.as_view(), name='continente_edit'),
    path('delete/<int:pk>', ContinenteDelete.as_view(), name='continente_delete'),

]
