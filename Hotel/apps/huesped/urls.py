from django.conf.urls import url, include
from apps.huesped.views import HuespedList,HuespedNew,HuespedUpdate,HuespedDelete,NacionalidadList,NacionalidadCreate

urlpatterns = [
    
    url(r'^listar', HuespedList.as_view(), name='huesped_listar'),
    url(r'^nuevo$',  HuespedNew.as_view(), name='huesped_agregar'),
    url(r'^editar/(?P<pk>\d+)$',  HuespedUpdate.as_view(), name='huesped_edit'),
    url(r'^eliminar/(?P<pk>\d+)$',  HuespedDelete.as_view(), name='huesped_delete'),
    url(r'^nacionalidad/listar', NacionalidadList.as_view(), name='nacionalidad_listar'),
    url(r'^nacionalidad/nueva$',  NacionalidadCreate.as_view(), name='nacionalidad_agregar'),
    # url(r'^teditar/(?P<pk>\d+)$',  NacionalidadUpdate.as_view(), name= 'nacionalidad_edit'),
    # url(r'^teliminarr/(?P<pk>\d+)$',  NacionalidadDelete.as_view(), name= 'nacionalidad_delete'),
]
