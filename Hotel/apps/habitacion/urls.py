from django.conf.urls import url
from apps.habitacion.views import index, habitacion_list, habitacion_new, habitacion_edit, habitacion_delete

urlpatterns =[
  url(r'^$',index),
  url(r'^listar/',habitacion_list,name="habitacion_listar"),
  url(r'^nuevo/',habitacion_new,name="habitacion_new"),
  url(r'^editar/(?P<id_habitacion>\d+)/',habitacion_edit, name="habitacion_editar"),
  url(r'^delete/(?P<id_habitacion>\d+)/',habitacion_delete, name="habitacion_eliminar"),
]