from django.urls import path

from apps.paises.views import *

urlpatterns = [
    path('list', PaisList.as_view(), name='pais_list'),
    path('detail/<int:pk>', PaisDetail.as_view(), name='pais_detail'),
    path('add', PaisCreate.as_view(), name='pais_create'),
    path('edit/<int:pk>', PaisUpdate.as_view(), name='pais_edit'),
    path('delete/<int:pk>', PaisDelete.as_view(), name='pais_delete'),

]
