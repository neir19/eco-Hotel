from django.conf.urls import url, include
from .views import HuespedList,HuespedNew,HuespedUpdate,HuespedDelete

urlpatterns = [
    
    url(r'^listar',HuespedList.as_view(), name='huesped_listar'),
    url(r'^nuevo$',  HuespedNew.as_view(), name='huesped_agregar'),
    url(r'^editar/(?P<pk>\d+)$',  HuespedUpdate.as_view(), name= 'huesped_edit'),
    url(r'^eliminar/(?P<pk>\d+)$',  HuespedDelete.as_view(), name= 'huesped_delete'),
]
