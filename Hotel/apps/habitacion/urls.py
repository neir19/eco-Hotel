from django.conf.urls import url
from apps.habitacion.views import index, HabitacionList,HabitacionDelete, HabitacionUpdate,HabitacionNew

urlpatterns =[
  url(r'^$',index),
  url(r'^listar/',HabitacionList.as_view(),name="habitacion_listar"),
  url(r'^nuevo/',HabitacionNew.as_view(),name="habitacion_new"),
  url(r'^editar/(?P<pk>\d+)/',HabitacionUpdate.as_view(), name="habitacion_editar"),
  url(r'^delete/(?P<pk>\d+)/',HabitacionDelete.as_view(), name="habitacion_eliminar"),
]